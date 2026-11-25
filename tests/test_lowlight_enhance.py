import pytest
import imaging.lowlight_enhance as mod

CASES = [
    ("noise_aware_gain", (1,)),
    ("temporal_stable", (1,)),
    ("chroma_split_denoise", (1,)),
    ("highlight_compress", (1,)),
    ("high_depth_process", (1,)),
    ("flicker_metric", (1,)),
    ("load", (1,)),
    ("enhance", (1,)),
    ("compose", (1,)),
    ("export", (1,)),
    ("validate_lowlight", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
