import numpy as np

def analyze_curve_shape(curve: list[float], tolerance: float = 1e-4) -> dict:
    peak_layer = int(np.argmax(curve))
    peak_value = float(curve[peak_layer])
    post_peak_slice = curve[peak_layer:]
    post_peak_min = float(min(post_peak_slice)) if len(post_peak_slice) > 0 else peak_value
    decay_amount = float(peak_value - post_peak_min)
    
    is_monotonic = all(curve[i] <= curve[i+1] + tolerance for i in range(len(curve)-1))
    return {
        "peak_layer": peak_layer,
        "peak_value": peak_value,
        "decay_amount": decay_amount,
        "is_monotonic_increasing": is_monotonic
    }

def gate_5v2_depth_aware(curve: list[float], claimed_layer: int, hard_cutoff_layer: int = 35) -> dict:
    shape_info = analyze_curve_shape(curve)
    decay = shape_info["decay_amount"]
    
    if claimed_layer > hard_cutoff_layer:
        if decay >= 0.10:
            return {"passed": True, "reason": "passed_late_with_decay"}
        return {"passed": False, "reason": "unlocalized_late_readout"}
        
    mid_slice = curve[12:29]
    mid_avg = sum(mid_slice) / len(mid_slice) if mid_slice else 0.0
    if curve[claimed_layer] < (mid_avg * 1.15) and curve[claimed_layer] < 0.30:
        return {"passed": False, "reason": "insufficient_mid_prominence"}
        
    return {"passed": True, "reason": "passed_localized_mid_circuit"}
