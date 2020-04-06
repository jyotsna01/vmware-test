FROM debian:buster

# Install additional Linux packages
RUN apt update --quiet \
  && apt install -y unzip wget \
  && apt install -y openvpn openssh-client \
  && apt install -y python3 python3-pip

# Install Google Chrome for UI test
RUN cd / \
  && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb --no-verbose \
  && apt install -y ./google-chrome-stable_current_amd64.deb \
  && rm google-chrome-stable_current_amd64.deb

# Install Google Cloud SDK
ENV CLOUDSDK_PYTHON=python3

# Populate Docker directory
RUN mkdir -p /vmware_test
COPY vmware_test/ /vmware_test/
RUN chmod -R +x /vmware_test/
WORKDIR /vmware_test/

# Install Python packages
RUN pip3 install --upgrade --requirement requirements.txt
