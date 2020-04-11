import numpy as np
from metrics import Metrics

def evaluate(model, test_loader, metrics):
    results = {m:[] for m in metrics}
    for batch_idx, (data_tr, heldout) in enumerate(test_loader):
        data_tensor = data_tr.view(data_tr.shape[0],-1)
        recon_batch = model.predict(data_tensor)[0].cpu().numpy()
        heldout = heldout.view(heldout.shape[0],-1).cpu().numpy()
        res = Metrics.compute(recon_batch, heldout, metrics)
        for m in res:
            results[m].append(res[m])

    for m in results:
        results[m] = np.concatenate(results[m])
    return results
