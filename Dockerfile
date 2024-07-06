# 1.ubuntu
FROM ubuntu:16.04
RUN apt-get -y update

# Install prerequisites
RUN apt-get -y install software-properties-common

# Add Brightbox PPA for Ruby
RUN apt-add-repository -y ppa:brightbox/ruby-ng

# Update package list again after adding new repository
RUN apt-get -y update

# Install Ruby and Bundler
RUN apt-get -y install ruby ruby-dev build-essential
RUN gem install bundler

# Source copy
COPY . /usr/src/app

# Gem package install
WORKDIR /usr/src/app
RUN bundle install

# Sinatra server run
EXPOSE 4567
CMD bundle exec ruby app.rb -o 0.0.0.0
