FROM python:3.7-slim

# Install sqlite3, git and cron 
RUN apt-get update -qq && apt-get install sqlite3 git cron -qq -y

# Install needed dependencies for Python 3.
RUN pip install --upgrade pip

# Our application directory on our Alpine image.
ENV APP_PATH /usr/src/app
RUN mkdir -p $APP_PATH

# Clone COVID-19 repo
WORKDIR $APP_PATH
RUN git clone https://github.com/CSSEGISandData/COVID-19.git

# Create sqlite database
WORKDIR $APP_PATH/core/flask_app/database
RUN sqlite3 covid19.sqlite3 .databases .quit

# Create a group app and a non-root user app to run our container.
WORKDIR $APP_PATH/core
RUN addgroup app && \
    adduser --disabled-password --gecos "" --ingroup app --no-create-home app

# Copy our requirement file to the workdir on our Alpine image and 
# process to install.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy content from our core/ directory to the workdir on our Alpine
# image so we've got the app ready to be launched.
COPY . .

# Run DB migrations and seed
RUN flask db upgrade && python manage.py seed

# Copy the cron to /etc/cron.d
ENV CRON /etc/cron.d
ENV COVID19_CRON $CRON/covid19-cron
COPY covid19-cron $COVID19_CRON

# Add exec permission to cron
RUN chmod 0644 $COVID19_CRON

# Apply cron job
RUN crontab $COVID19_CRON

# Create cron log
RUN touch /var/log/cron.log

# Run the cron
CMD /usr/sbin/cron -f

# Switch to our app user.
USER app
