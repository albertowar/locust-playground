FROM python:3

#==============
# Expose Ports
#==============
EXPOSE 5557
EXPOSE 5558

#======================
# Install dependencies
#======================
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

#=====================
# Start docker-locust
#=====================
COPY src /src/

CMD ["locust", "-f", "src/locustfile.py", "--slave", "--master-host=master"]
