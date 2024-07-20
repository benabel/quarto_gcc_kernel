from ipykernel.kernelbase import Kernel
from .utils import compile_run_c, handle_metadata


class GccKernel(Kernel):
    # doc: https://ipykernel.readthedocs.io/en/stable/index.html
    implementation = "Gcc"
    implementation_version = "1.0"
    language = "c"
    language_version = "0.1"
    language_info = {
        "name": "gcc",
        "mimetype": "text/x-c",
        "file_extension": ".c",
    }
    banner = "Gcc kernel - as useful as a parrot"

    # In order to receive metadata information from Quarto,
    # a kernel must implement the `comm_open` handler
    # and add it to the `shell_handlers` dictionary during initialization
    def comm_open(self, stream, ident, msg):
        msg = msg["content"]
        if msg["target_name"] == "quarto_kernel_setup":
            # here, msg['data']['options'] has all quarto setup options
            pass
        # TODO: close comm as needed

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shell_handlers["comm_open"] = self.comm_open

    def do_execute(
        self, code, silent, store_history=True, user_expressions=None, allow_stdin=False
    ):
        # This is where the kernel executes code
        # In a real kernel, you would call the appropriate
        # code execution library here (e.g. a C compiler)
        # and return the result
        # run c compiler and stream output
        metadata_dict, code = handle_metadata(code)
        if not silent:
            stream_content = {
                "name": "stdout",
                "text": compile_run_c(code, metadata_dict),
            }
            self.send_response(self.iopub_socket, "stream", stream_content)

        # in this example, we are using a very simple way to
        # detect if a cell is a setup cell. In a real kernel, you
        # would want to use a more robust method to detect setup cells
        # (like a UUID sent as the code)

        is_setup_cell = (
            code.strip() == "setup"
        )  # use whatever check is appropriate for your kernel here
        if is_setup_cell:
            # If this is a setup cell, quarto will ignore the output
            # (except for the metadata). Still, `execute_result` needs
            # something to send, so we send an empty string
            self.send_response(
                self.iopub_socket,
                "execute_result",
                {
                    "data": {"text/x-c": ""},
                    "metadata": {"quarto": {"daemonize": True}},
                    "execution_count": self.execution_count,
                },
            )

        return {
            "status": "ok",
            # The base class increments the execution count
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {},
        }
