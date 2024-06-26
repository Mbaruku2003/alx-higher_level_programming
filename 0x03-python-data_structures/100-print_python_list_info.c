#include <Python.h>
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (pyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, PY_TYPE (obj->ob_item[i])->tp_name);
}
