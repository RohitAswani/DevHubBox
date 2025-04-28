# Use the official Node.js image from Docker Hub
FROM node:latest

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install the app dependencies
RUN npm install

# Copy the rest of the app files
COPY . .

# Expose port 3000 to access the app
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]