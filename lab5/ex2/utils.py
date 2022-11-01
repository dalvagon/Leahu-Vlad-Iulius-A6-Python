def list_sum(*l, **kl):
    return sum([kl[k] for k in kl.keys()])


lambda_list_sum = lambda *l, **kl: sum([kl[k] for k in kl.keys()])
