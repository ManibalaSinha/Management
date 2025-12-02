# Base image
FROM node:20

# Set working directory
WORKDIR /usr/src/app

# Copy package files
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install

# Copy frontend code
COPY . .

# Expose port
EXPOSE 3000

# Start React in development mode
CMD ["yarn", "start"]
