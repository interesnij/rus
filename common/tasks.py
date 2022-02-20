from tr.celery import app

@app.task(bind=True, max_retries=5)
def abort_suspended(list):
    item = list[0]
    if item.is_suspended():
        return
    else:
        return item.unsuspend_item()
