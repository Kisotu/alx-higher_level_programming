#include <object.h>
#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - func that prints basic info abt python lists
 * @p: python list
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int k;
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (k = 0; k < size; k++)
		printf("Element %i: %s\n", k, Py_Type(obj->ob_item[k])->tp_name);
}
