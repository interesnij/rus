def get_good_processing(video, status):
    video.status = status
    video.save(update_fields=['status'])
    return video
def get_good_list_processing(list, status):
    list.type = status
    list.save(update_fields=['type'])
    return list
