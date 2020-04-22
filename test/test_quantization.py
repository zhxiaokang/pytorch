# -*- coding: utf-8 -*-

from torch.testing._internal.common_utils import run_tests

# Quantized Tensor
from quantization.test_quantized_tensor import TestQuantizedTensor  # noqa: F401
# Quantized Op
# TODO: merge test cases in quantization.test_quantized
from quantization.test_quantized_op import TestQuantizedOps  # noqa: F401
from quantization.test_quantized_op import TestQNNPackOps  # noqa: F401
from quantization.test_quantized_op import TestQuantizedLinear  # noqa: F401
from quantization.test_quantized_op import TestDynamicQuantizedLinear  # noqa: F401
from quantization.test_quantized_op import TestComparatorOps  # noqa: F401
# Quantized Functional and Module
# TODO: split functional
from quantization.test_quantized_module import TestFunctional  # noqa: F401
from quantization.test_quantized_module import TestStaticQuantizedModule  # noqa: F401
from quantization.test_quantized_module import TestDynamicQuantizedModule  # noqa: F401

# Quantization aware training
from quantization.test_fake_quant import TestFakeQuantizePerTensor  # noqa: F401
from quantization.test_fake_quant import TestFakeQuantizePerChannel  # noqa: F401
from quantization.test_qat_module import TestQATModule  # noqa: F401

# Workflow
from quantization.test_quantize import TestPostTrainingStatic  # noqa: F401
from quantization.test_quantize import TestPostTrainingDynamic  # noqa: F401
from quantization.test_quantize import TestQuantizationAwareTraining  # noqa: F401
# TODO: move to test_quantize_script
from quantization.test_quantize import TestGraphModePostTrainingStatic  # noqa: F401
# TODO: move to test_quantized_module
from quantization.test_quantize import TestFunctionalModule  # noqa: F401
from quantization.test_quantize import TestFusion  # noqa: F401
from quantization.test_quantize import TestObserver  # noqa: F401
# TODO: merge with TestObserver
from quantization.test_quantize import TestRecordHistogramObserver  # noqa: F401
from quantization.test_quantize_script import TestQuantizeScriptJitPasses  # noqa: F401
from quantization.test_quantize_script import TestQuantizeScriptPTSQOps  # noqa: F401
from quantization.test_quantize_script import TestQuantizeDynamicScript  # noqa: F401

# Model numerics
# TODO: move to test_quantize
from quantization.test_numerics import TestModelNumerics  # noqa: F401

# Tooling: numric_suite
from quantization.test_numeric_suite import TestEagerModeNumericSuite  # noqa: F401

# Backward Compatibility
from quantization.test_backward_compatibility import TestSerialization  # noqa: F401

if __name__ == '__main__':
    run_tests()
