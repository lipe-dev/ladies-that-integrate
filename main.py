# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import playsound

from argparser import parse_args
from endpoints import request_jobs, update_jobs
from photoshop import job_to_image

if __name__ == '__main__':
    args = parse_args()

    print("Mission Start!")
    print()

    jobs = request_jobs(args.app, args.key)

    print("Processing Jobs' Images")
    for job in jobs:
        if not job.get("fields").get("Imagem") or args.all_images:
            job_to_image(job)

    if len(jobs) > 0:
        update_jobs(args.app, args.key, jobs)
    else:
        print("There is no new jobs for now. If there should be any, check your AirTable.")

    print()
    print("Mission Complete! Respect +")

    playsound.playsound("gtasa.mp3", True)
