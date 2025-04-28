
# Reflection Document

## Project Overview
This project focused on building and enhancing a **User Management** system with various improvements, including a major feature: **Profile Picture Upload with Minio**.

Throughout this project, I have learned:
- How to integrate **object storage** solutions like **Minio** into FastAPI applications.
- How to set up **Docker** environments for local development and production.
- How to build robust **CI/CD pipelines** with **GitHub Actions** for testing, building, pushing Docker images, and scanning vulnerabilities.
- Best practices in **test-driven development** by adding and validating **QA issue fixes** and **new tests**.
- Troubleshooting Git issues like `.git` corruption and recovering repository history safely.

## Key Deliverables

| Requirement | Delivered |
|:---|:---|
| **Feature Implemented** | [Profile Picture Upload with Minio](https://github.com/varshith-29/user_management/commit/8e4f1df) |
| **DockerHub Deployment** | [Docker Repository Link](https://hub.docker.com/repository/docker/varshithveluru/user_management/general) |
| **QA Issues** | [Closed via commits fixing pytest issues and password validation](https://github.com/varshith-29/user_management/pull/7) |
| **New Tests** | [Tests added for Profile Picture Upload](https://github.com/varshith-29/user_management/commit/4052b68) |
| **Successful CI/CD Pipeline** | GitHub Actions set up for tests, Docker build, and vulnerability scanning |

## Highlighted Commits & Pull Requests
- **Profile Picture Upload Feature**:
  - [Commit: Added Endpoint for Profile Picture Upload using Minio](https://github.com/varshith-29/user_management/commit/8e4f1df)
  - [Commit: Added Tests for Profile Picture Upload](https://github.com/varshith-29/user_management/commit/4052b68)
  - [Commit: Added Minio setup using Docker](https://github.com/varshith-29/user_management/commit/3dfc356)

- **Password Validation QA Fix**:
  - [Pull Request: Password must be 8-24 characters long with required constraints](https://github.com/varshith-29/user_management/pull/8)

- **CI/CD Implementation**:
  - Build, Test, Push to DockerHub and Scan using Trivy (integrated in `.github/workflows/ci-cd.yml`).

## Feature Description: Profile Picture Upload with Minio
- **API endpoint** created to allow users to upload their profile pictures.
- **Minio** is used as a backend **object storage** to securely store pictures.
- **User Profile API** updated to include a **profile picture URL**.
- **Image validation** is included to restrict the allowed image formats and sizes.
- **Optional Enhancements** implemented:
  - Support for default profile picture for users without uploads.

# Final Submission Summary
- 🚀 Code passes local unit tests.
- 🚀 Application pushed successfully to DockerHub.
- 🚀 Reflection document created summarizing major learnings and accomplishments.
- 🚀 Project and major issues clearly traceable via commits and PR links.

# References
- [DockerHub Repository](https://hub.docker.com/repository/docker/varshithveluru/user_management/general)
- [GitHub Repository](https://github.com/varshith-29/user_management)
