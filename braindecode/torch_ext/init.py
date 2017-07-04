from torch.nn import init


def glorot_weight_zero_bias(model):
    for module in model.modules():
        if hasattr(module, 'weight'):
            if not ('BatchNorm' in module.__class__.__name__):
                init.xavier_uniform(module.weight, gain=1)
            else:
                init.constant(module.weight, 1)
        if hasattr(module, 'bias'):
            if module.bias is not None:
                init.constant(module.bias, 0)