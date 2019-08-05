import heapq


def get_running_medians(arr):
    if len(arr) is 0:
        return []
    elif len(arr) is 1:
        return [arr[0]]
    else:
        return build_running_medians(arr)


def build_running_medians(arr):
    (medians, min_heap, max_heap) = ([], [], [])
    medians.append(arr[0])
    heapq.heappush(min_heap, arr[0])
    for i in range(1, len(arr)):
        (elem, last_median) = (arr[i], medians[-1])
        if elem < last_median:
            # max_heap candidate
            add_to_max_heap_if_allows(elem, max_heap, min_heap)
        else:
            # min_heap candidate
            add_to_min_heap_if_allows(elem, min_heap, max_heap)
        medians.append(get_median(min_heap, max_heap))
    return medians


def add_to_max_heap_if_allows(elem, max_h, min_h):
    if len(max_h) - len(min_h) <= 0:
        heappush_max(max_h, elem)
    else:
        # max_h is too big
        if get_max_heap_root(max_h) <= elem:
            heapq.heappush(min_h, elem)
        else:
            max_root = heappop_max(max_h)
            heappush_max(max_h, elem)
            heapq.heappush(min_h, max_root)


def add_to_min_heap_if_allows(elem, min_h, max_h):
    if len(min_h) - len(max_h) <= 0:
        heapq.heappush(min_h, elem)
    else:
        # min_h is too big
        if min_h[0] >= elem:
            heappush_max(max_h, elem)
        else:
            min_root = heapq.heappop(min_h)
            heapq.heappush(min_h, elem)
            heappush_max(max_h, min_root)


def heappush_max(max_h, el):
    heapq.heappush(max_h, el * -1)


def get_max_heap_root(max_h):
    return max_h[0] * -1


def heappop_max(max_h):
    return heapq.heappop(max_h) * -1


def get_median(min_h, max_h):
    if len(max_h) > len(min_h):
        return get_max_heap_root(max_h)
    elif len(min_h) > len(max_h):
        return min_h[0]
    elif len(min_h) is 0 and len(max_h) is 0:
        return None
    else:
        return (get_max_heap_root(max_h) + min_h[0]) / 2

