FROM python:3.7-slim

# Install needed dependencies for Python 3.
RUN pip install --upgrade pip

# Our application directory on our Alpine image.
ENV APP_PATH /usr/src/app
RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH/core

# Create a group app and a non-root user app to run our container.
RUN addgroup app && \
    adduser --disabled-password --gecos "" --ingroup app --no-create-home app

# Copy our requirement file to the workdir on our Alpine image and 
# process to install.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy content from our core/ directory to the workdir on our Alpine
# image so we've got the app ready to be launched.
COPY . .

# Switch to our app user.
USER app
