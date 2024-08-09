import time


def rate_limiter(max_allowed_calls, reset_period_seconds):
    def decorate_rate_limited_function(original_function):
        calls_count = 0
        last_reset_time = time.time()

        def wrapper_function(*args, **kwargs):
            nonlocal calls_count, last_reset_time
            elapsed_time = time.time() - last_reset_time

            # If the elapsed time is greater than the reset period, reset the call count
            if elapsed_time > reset_period_seconds:
                calls_count = 0
                last_reset_time = time.time()

            # Check if the call count has reached the maximum allowed limit
            if calls_count >= max_allowed_calls:
                raise Exception("Rate limit exceeded. Please try again later.")

            # Increment the call count
            calls_count += 1

            # Call the original function
            return original_function(*args, **kwargs)

        return wrapper_function

    return decorate_rate_limited_function


# Allowing a maximum of 6 API calls within 10 seconds.
@rate_limiter(max_allowed_calls=6, reset_period_seconds=10)
def make_api_call():
    print("API call executed successfully...")


# Make API calls
for _ in range(8):
    try:
        make_api_call()
    except Exception as error:
        print(f"Error occurred: {error}")
time.sleep(10)
make_api_call()
