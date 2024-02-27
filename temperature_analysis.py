from mrjob.job import MRJob
from mrjob.step import MRStep

class MRTemperatureAnalysis(MRJob):

    def configure_args(self):
        super(MRTemperatureAnalysis, self).configure_args()
        self.add_passthru_arg('--target-date', type=str, help='Target date for temperature analysis', default='20240101')

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        # Split the CSV line
        parts = line.split(',')
        if len(parts) > 3:
            station_id, date, element_type, value = parts[0], parts[1], parts[2], parts[3]
            if date == self.options.target_date and element_type in ['TMAX', 'TMIN']:
                yield (station_id, element_type), float(value)

    def reducer(self, key, values):
        values_list = list(values)
        avg_value = sum(values_list) / len(values_list)
        yield key, avg_value

if __name__ == '__main__':
    MRTemperatureAnalysis.run()