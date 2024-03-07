FROM gitpod/workspace-mysql

USER gitpod

RUN /bin/bash -c "apt-get update \
        && apt-get install -y python3 python3-pip \
        && pip3 install -r /path/to/your/project/requirements.txt \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*"

