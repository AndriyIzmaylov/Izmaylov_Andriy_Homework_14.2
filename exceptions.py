class GroupLimitError(Exception):

    def __init__(self, message="Group limit reached. Cannot add more than 10 students."):
        super().__init__(message)
