from collections import deque

class PrinterQueue:
    def __init__(self):
        self.jobs = deque()

    def add_job(self, job):
        print(f"Adding job: {job}")
        self.jobs.append(job)

    def print_job(self):
        if self.jobs:
            job = self.jobs.popleft()
            print(f"Printing job: {job}")
        else:
            print("No jobs to print")

# Example usage
printer_queue = PrinterQueue()
printer_queue.add_job("Document1.pdf")
printer_queue.add_job("Document2.docx")
printer_queue.add_job("Document3.pptx")

printer_queue.print_job()
printer_queue.print_job()
printer_queue.print_job()
