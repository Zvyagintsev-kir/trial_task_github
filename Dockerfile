FROM python:2.7
#RUN useradd -ms /bin/bash admin
WORKDIR /trial_task_github
#RUN pip install -r requirements.txt
CMD ["sleep", "1000"]