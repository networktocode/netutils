// Forwards the execution to the python script
const py_run = Deno.run({
    // Run `python ./flat_postprocess/protocol_number_postprocess.py netutils/data_files/protocol_number_mappings.py` to test locally.
    cmd: ["python", "./flat_postprocess/protocol_number_postprocess.py"].concat(Deno.args),
});

await py_run.status();
