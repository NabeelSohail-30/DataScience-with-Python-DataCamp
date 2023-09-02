# Add a decorator that will make timer() a context manager
@contextlib.contextmanager()
def timer():
    """Time the execution of a context block.

    Yields:
      None
    """
    start = time.time()
    # Send control back to the context block
    ____
    end = time.time()
    print('Elapsed: {:.2f}s'.format(end - start))


with timer():
    print('This should take approximately 0.25 seconds')
    time.sleep(0.25)
