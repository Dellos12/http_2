
import numpy as np
import os

# Trava de segurança para CPUs no Jenkins/Docker
os.environ['POLARS_SKIP_CPU_CHECK'] = '1'

def apply_patches():
    compat_map = {
        'bool': bool, 'int': int, 'float': float, 'object': object,
        'Inf': np.inf, 'INF': np.inf, 'infty': np.inf, 'PZERO': 0.0,
        'alltrue': np.all, 'sometrue': np.any, 'round_': np.round,
        'product': np.prod, 'product_': np.prod, 'cumproduct_': np.cumprod,
        'alen': lambda x: len(x)
    }
    for attr, value in compat_map.items():
        if not hasattr(np, attr):
            setattr(np, attr, value)
    print("✅ Patch de Geometria Numpy/MXNet aplicado.")

apply_patches()
