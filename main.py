import re

workers_stats_rows = [
    "Андрей 9",
    "Василий 11",
    "Роман 7",
    "X Æ A-12 45",
    "Иван Петров 3",
    "Андрей 6",
    "Роман 11",
]


def get_statistics(workers_stats_rows: list[str]) -> list[str]:
    workers_dict: dict[str, list[str, int]] = {}

    for worker_stats_row in workers_stats_rows:
        number: str | int = ""
        worker_name: str = ""

        number = re.findall('\\s([^\\s]*)$', worker_stats_row)[0]
        worker_name = worker_stats_row[0:-len(number)]

        # for i in range((len(worker_stats_row) - 1), 0, -1):
        #     if worker_stats_row[i] == " ":
        #         worker_name = worker_stats_row[0:i]
        #         break
        #
        #     number = worker_stats_row[i] + number

        if workers_dict.get(worker_name) is not None:
            workers_dict[worker_name][0] = workers_dict[worker_name][0] + f", {number}"
            workers_dict[worker_name][1] = workers_dict[worker_name][1] + int(number)
            break

        workers_dict[worker_name] = [number, int(number)]

    counted_workers_data_list = []
    for key in workers_dict.keys():
        worker_stats_row = (
                key + f" {workers_dict[key][0]}; sum: {workers_dict[key][1]}"
        )
        counted_workers_data_list.append(worker_stats_row)

    print('\n'.join(counted_workers_data_list))

    return counted_workers_data_list


get_statistics(workers_stats_rows)

if __name__ == 'main':
    get_statistics(workers_stats_rows)
