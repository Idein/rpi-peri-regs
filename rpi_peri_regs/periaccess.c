#include <Python.h>

static PyObject* periaccess_read4(PyObject *self, PyObject *args)
{
    /* int and long are both 32-bit on both A32 and A64.
     * http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.den0024a/ch08s02.html
     */
    unsigned addr, val;

    if (!PyArg_ParseTuple(args, "I", &addr))
        return NULL;

    /* For constraints, see https://gcc.gnu.org/onlinedocs/gcc/Constraints.html
     */
    asm volatile (
            "ldr %[val], [%[addr]]\n\t"
            : [val] "=r" (val)
            : [addr] "r" (addr)
            : "memory"
    );

    return PyLong_FromUnsignedLong(val);
}

static PyObject* periaccess_write4(PyObject *self, PyObject *args)
{
    unsigned addr, val;

    if (!PyArg_ParseTuple(args, "II", &addr, &val))
        return NULL;

    asm volatile (
            "str %[val], [%[addr]]\n\t"
            :
            : [addr] "r" (addr),
              [val] "r" (val)
            : "memory"
    );

    Py_RETURN_NONE;
}

static PyMethodDef PeriaccessMethods[] = {
    {"read4", periaccess_read4, METH_VARARGS, "Read 4 bytes."},
    {"write4", periaccess_write4, METH_VARARGS, "Write 4 bytes."},
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef periaccessmodule = {
    PyModuleDef_HEAD_INIT,
    "periaccess",
    NULL,
    -1,
    PeriaccessMethods,
};

PyMODINIT_FUNC PyInit_periaccess(void)
{
    return PyModule_Create(&periaccessmodule);
}

int main(int argc, char *argv[])
{
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL){
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }

    PyImport_AppendInittab("periaccess", PyInit_periaccess);
    Py_SetProgramName(program);
    Py_Initialize();
    PyImport_ImportModule("periaccess");

    PyMem_RawFree(program);
    return 0;
}
