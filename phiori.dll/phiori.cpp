#include <Windows.h>
#include <Python.h>

const char *SHIORI_RESPONSE_200 = "SHIORI/3.0 200 OK\r\nValue: ";
const char *CRLF = "\r\n";

char dllRoot[MAX_PATH];
PyObject *mainModule;
PyObject *phioriModule;
PyObject *globalDict;
PyObject *phioriDict;

char *getException(long *len);

extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len) {
	memcpy(dllRoot, (char *)GlobalLock(h), len);
	GlobalFree(h);
	char libRoot[MAX_PATH * 2];
	sprintf(libRoot, "%s;%s\\lib.zip", dllRoot, dllRoot);
	_putenv_s("PYTHONPATH", libRoot);
	Py_Initialize();
	mainModule = PyImport_AddModule("__main__");
	phioriModule = PyImport_ImportModule("phiori");
	PyObject_SetAttrString(mainModule, "_phiori", phioriModule);
	globalDict = PyModule_GetDict(mainModule);
	phioriDict = PyModule_GetDict(phioriModule);
	PyObject *func = PyDict_GetItemString(phioriDict, "load");
	PyObject *arg0 = PyUnicode_FromStringAndSize(dllRoot, len);
	PyObject *arg1 = PyLong_FromLong(len);
	PyObject *args = PyTuple_Pack(2, arg0, arg1);
	PyObject *result = PyObject_CallObject(func, args);
	BOOL _result = TRUE;
	if (result != NULL)
		_result = PyObject_IsTrue(result);
	Py_XDECREF(result);
	Py_XDECREF(args);
	Py_XDECREF(arg1);
	Py_XDECREF(arg0);
	result = args = arg1 = arg0 = NULL;
	return _result;
}

extern "C" __declspec(dllexport) BOOL __cdecl unload(void) {
	PyObject *func = PyDict_GetItemString(phioriDict, "unload");
	PyObject *args = PyTuple_New(0);
	PyObject *result = PyObject_CallObject(func, args);
	BOOL _result = TRUE;
	if (result != NULL)
		_result = PyObject_IsTrue(result);
	Py_XDECREF(result);
	Py_XDECREF(args);
	result = args = NULL;
	Py_Finalize();
	return _result;
}

extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len) {
	try {
		char *req = (char *)malloc(*len);
		memcpy(req, (char *)h, *len);
		GlobalFree(h);
		PyObject *func = PyDict_GetItemString(phioriDict, "request");
		PyObject *arg0 = PyUnicode_FromStringAndSize(req, *len);
		PyObject *arg1 = PyLong_FromLong(*len);
		PyObject *args = PyTuple_Pack(2, arg0, arg1);
		PyObject *result = PyObject_CallObject(func, args);
		if (PyErr_Occurred()) {
			long errlen;
			char *err = getException(&errlen);
			char *ss = "\\0";
			char *result = (char *)malloc(strlen(SHIORI_RESPONSE_200) + strlen(ss) + strlen(err) + strlen(CRLF) + strlen(CRLF));
			strcat(result, SHIORI_RESPONSE_200);
			strcat(result, ss);
			strcat(result, err);
			strcat(result, CRLF);
			strcat(result, CRLF);
			*len = strlen(result);
			HGLOBAL hResult = GlobalAlloc(GMEM_FIXED, *len);
			memcpy((char *)hResult, result, *len);
			return hResult;
		}
		free(req);
		char *_result = PyUnicode_AsUTF8(result);
		*len = strlen(_result);
		HGLOBAL hResult = GlobalAlloc(GMEM_FIXED, *len);
		memcpy((char *)hResult, _result, *len);
		Py_XDECREF(result);
		Py_XDECREF(args);
		Py_XDECREF(arg1);
		Py_XDECREF(arg0);
		result = args = arg1 = arg0 = NULL;
		if (*len > 0)
			return hResult;
		GlobalFree(hResult);
	}
	catch (DWORD dwError) {
		try {
			long errlen;
			char *err = getException(&errlen);
			char *ss = "\\0";
			char *result = (char *)malloc(strlen(SHIORI_RESPONSE_200) + strlen(ss) + strlen(err) + strlen(CRLF) + strlen(CRLF));
			strcat(result, SHIORI_RESPONSE_200);
			strcat(result, ss);
			strcat(result, err);
			strcat(result, CRLF);
			strcat(result, CRLF);
			*len = strlen(result);
			HGLOBAL hResult = GlobalAlloc(GMEM_FIXED, *len);
			memcpy((char *)hResult, result, *len);
			return hResult;
		}
		catch (DWORD dwError) {
			*len = 0;
			return NULL;
		}
	}
	*len = 0;
	return NULL;
}

char *getException(long *len) {
	PyObject *type;
	PyObject *value;
	PyObject *traceback;
	PyErr_Fetch(&type, &value, &traceback);
	PyErr_Clear();
	return PyUnicode_AsUTF8(value);
}
