# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
RUN npm install react-scripts@3.0.1 -g --silent
COPY ./package.json /app
COPY ./package-lock.json /app
RUN npm ci
COPY . /app

# start app
CMD ["npm", "start"]
