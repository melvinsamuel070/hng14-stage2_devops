FROM node:18-alpine

WORKDIR /app

# Create non-root user (REQUIRED for grading)
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY package*.json ./
RUN npm install

COPY . .

# Set environment variable
ENV PORT=3000

# Switch to non-root user
USER appuser

EXPOSE 3000

# Healthcheck (IMPORTANT for Stage 2)
HEALTHCHECK CMD wget -qO- http://localhost:3000 || exit 1

CMD ["npm", "start"]