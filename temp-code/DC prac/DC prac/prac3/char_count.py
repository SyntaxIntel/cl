from mrjob.job import MRJob

class MRCharacterCount(MRJob):
    
    def mapper(self, _, line):
        """Mapper function: Processes each line and emits (char, 1) for each character."""
        for char in line:
            if char.isalnum():  # Consider only letters and digits
                yield char.lower(), 1  # Convert to lowercase for uniformity

    def reducer(self, key, values):
        """Reducer function: Aggregates character counts."""
        yield key, sum(values)

if __name__ == '__main__':
    MRCharacterCount.run()
