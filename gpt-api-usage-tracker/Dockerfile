# Base image
FROM node:14-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire project
COPY . .

EXPOSE 3000

# Set the command to run the app
CMD npm start
# Expose the port the app will run on
