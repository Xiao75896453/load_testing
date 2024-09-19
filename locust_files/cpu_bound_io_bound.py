import time

from locust import HttpUser, between, task


class UserOrScenario(HttpUser):
    wait_time = between(1, 5)

    @task
    def task1(self):
        self.client.get("/hello")
        self.client.get("/world")

    @task(3)
    def task2(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}")
            time.sleep(1)


class CPUBoundAsync(HttpUser):
    @task
    def cpu_bound_async(self):
        self.client.get("/api/cpu_bound/async")


class CPUBoundSync(HttpUser):
    @task
    def cpu_bound_sync(self):
        self.client.get("/api/cpu_bound/sync")


class IOBoundAsyncCreate(HttpUser):
    @task
    def io_bound_async_create(self):
        self.client.post("/api/io_bound/async")


class IOBoundAsyncGet(HttpUser):
    @task
    def io_bound_async_get(self):
        self.client.get("/api/io_bound/async")


class IOBoundAsyncHelloWorld(HttpUser):
    @task
    def io_bound_async_hello_world(self):
        self.client.get("/api/io_bound/async/hello_world")


class IOBoundAsyncUpdate(HttpUser):
    @task
    def io_bound_async_update(self):
        self.client.patch("/api/io_bound/async")


class IOBoundSyncCreate(HttpUser):
    @task
    def io_bound_sync_create(self):
        self.client.post("/api/io_bound/sync")


class IOBoundSyncGet(HttpUser):
    @task
    def io_bound_sync_get(self):
        self.client.get("/api/io_bound/sync")


class IOBoundSyncHelloWorld(HttpUser):
    @task
    def io_bound_sync_hello_world(self):
        self.client.get("/api/io_bound/sync/hello_world")


class IOBoundSyncUpdate(HttpUser):
    @task
    def io_bound_sync_update(self):
        self.client.patch("/api/io_bound/sync")
