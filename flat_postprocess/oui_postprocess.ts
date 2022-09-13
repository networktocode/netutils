// Forwards the execution to the python script
const py_run = Deno.run({
    cmd: ['python', './flat_postprocess/oui_postprocess.py'].concat(Deno.args),
});

await py_run.status();
