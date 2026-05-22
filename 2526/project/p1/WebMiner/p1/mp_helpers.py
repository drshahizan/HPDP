# mp_helpers.py
# Worker functions for multiprocessing pool.
# Must be in a separate file — Windows multiprocessing spawns fresh Python
# processes that re-import __main__. In Jupyter, __main__ is the kernel,
# which causes the pool to hang. A separate module avoids this entirely.

import pandas as pd

CURRENT_YEAR = 2026

def process_chunk(args):
    """
    Runs in each worker process.
    Applies filter + feature engineering on one DataFrame chunk.
    """
    chunk_df, _ = args

    filtered = chunk_df[
        (chunk_df['mileage_km'] < 100_000) &
        (chunk_df['condition'] == 'Used') &
        (chunk_df['price_myr'] > 0)
    ].copy()

    filtered['price_per_km']   = filtered['price_myr'] / (filtered['mileage_km'] + 1)
    filtered['car_age']        = CURRENT_YEAR - filtered['year']
    filtered['price_per_year'] = filtered['price_myr'] / (filtered['car_age'] + 1)

    return filtered
