[     UTC     ] Logs for alex-optimisation-demo-fxpcgdhfpiwuijpxuyw9qx.streamlit.app/

────────────────────────────────────────────────────────────────────────────────────────

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:48:36.087 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:48:36.422 503 GET /script-health-check (127.0.0.1) 458.25ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:48:41.109 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:48:41.448 503 GET /script-health-check (127.0.0.1) 445.00ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:48:46.122 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:48:46.459 503 GET /script-health-check (127.0.0.1) 469.56ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:48:51.076 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:48:51.412 503 GET /script-health-check (127.0.0.1) 418.95ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:48:56.072 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:48:56.403 503 GET /script-health-check (127.0.0.1) 429.49ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:49:01.054 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:49:01.408 503 GET /script-health-check (127.0.0.1) 445.35ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:49:06.113 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:49:06.463 503 GET /script-health-check (127.0.0.1) 490.35ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:49:11.149 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:49:11.476 503 GET /script-health-check (127.0.0.1) 469.13ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:49:16.119 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:49:16.456 503 GET /script-health-check (127.0.0.1) 463.12ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:49:21.080 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:49:21.412 503 GET /script-health-check (127.0.0.1) 456.46ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:49:26.024 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:49:26.378 503 GET /script-health-check (127.0.0.1) 461.52ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:49:31.115 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:49:31.489 503 GET /script-health-check (127.0.0.1) 510.05ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:49:36.107 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:49:36.438 503 GET /script-health-check (127.0.0.1) 450.50ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:49:41.095 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:49:41.431 503 GET /script-health-check (127.0.0.1) 460.91ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:49:46.113 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:49:46.513 503 GET /script-health-check (127.0.0.1) 532.05ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:49:51.119 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:49:51.466 503 GET /script-health-check (127.0.0.1) 488.38ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:49:56.091 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:49:56.441 503 GET /script-health-check (127.0.0.1) 452.21ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:50:01.089 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:50:01.421 503 GET /script-health-check (127.0.0.1) 468.64ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:50:06.105 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:50:06.467 503 GET /script-health-check (127.0.0.1) 501.04ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:50:11.120 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:50:11.477 503 GET /script-health-check (127.0.0.1) 498.79ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:50:16.062 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:50:16.421 503 GET /script-health-check (127.0.0.1) 447.96ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:50:21.060 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:50:21.410 503 GET /script-health-check (127.0.0.1) 446.33ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:50:26.120 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:50:26.495 503 GET /script-health-check (127.0.0.1) 510.88ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:50:31.103 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:50:31.470 503 GET /script-health-check (127.0.0.1) 507.87ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:50:36.089 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:50:36.434 503 GET /script-health-check (127.0.0.1) 435.47ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:50:41.102 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:50:41.435 503 GET /script-health-check (127.0.0.1) 470.20ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:50:46.114 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:50:46.461 503 GET /script-health-check (127.0.0.1) 466.14ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:50:51.085 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:50:51.435 503 GET /script-health-check (127.0.0.1) 438.32ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:50:56.129 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:50:56.490 503 GET /script-health-check (127.0.0.1) 501.72ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:51:01.114 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:51:01.483 503 GET /script-health-check (127.0.0.1) 501.11ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:51:06.098 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:51:06.429 503 GET /script-health-check (127.0.0.1) 433.79ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:51:11.105 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:51:11.439 503 GET /script-health-check (127.0.0.1) 449.66ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:51:16.147 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:51:16.492 503 GET /script-health-check (127.0.0.1) 488.72ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:51:21.081 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:51:21.428 503 GET /script-health-check (127.0.0.1) 475.09ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:51:26.070 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:51:26.409 503 GET /script-health-check (127.0.0.1) 423.68ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:51:31.091 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:51:31.421 503 GET /script-health-check (127.0.0.1) 456.63ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:51:36.078 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:51:36.431 503 GET /script-health-check (127.0.0.1) 476.07ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:51:40.990 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:51:41.339 503 GET /script-health-check (127.0.0.1) 432.57ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:51:46.117 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:51:46.450 503 GET /script-health-check (127.0.0.1) 463.62ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:51:51.102 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:51:51.434 503 GET /script-health-check (127.0.0.1) 430.26ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:51:56.094 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:51:56.439 503 GET /script-health-check (127.0.0.1) 485.18ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:52:01.027 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:52:01.397 503 GET /script-health-check (127.0.0.1) 484.77ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:52:06.092 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:52:06.421 503 GET /script-health-check (127.0.0.1) 452.85ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:52:11.219 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:52:11.565 503 GET /script-health-check (127.0.0.1) 479.16ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:52:16.091 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:52:16.441 503 GET /script-health-check (127.0.0.1) 464.03ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:52:21.095 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:52:21.430 503 GET /script-health-check (127.0.0.1) 444.79ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:52:26.127 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:52:26.471 503 GET /script-health-check (127.0.0.1) 487.18ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:52:31.136 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:52:31.466 503 GET /script-health-check (127.0.0.1) 463.20ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:52:36.068 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:52:36.428 503 GET /script-health-check (127.0.0.1) 454.21ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:52:41.100 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:52:41.474 503 GET /script-health-check (127.0.0.1) 511.31ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:52:46.066 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:52:46.395 503 GET /script-health-check (127.0.0.1) 430.96ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:52:51.072 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:52:51.431 503 GET /script-health-check (127.0.0.1) 490.83ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:52:56.106 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:52:56.434 503 GET /script-health-check (127.0.0.1) 466.96ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:53:01.094 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:53:01.441 503 GET /script-health-check (127.0.0.1) 484.60ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:53:06.050 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:53:06.384 503 GET /script-health-check (127.0.0.1) 426.19ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:53:11.077 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:53:11.459 503 GET /script-health-check (127.0.0.1) 510.77ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:53:16.127 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:53:16.487 503 GET /script-health-check (127.0.0.1) 498.65ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:53:21.070 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:53:21.423 503 GET /script-health-check (127.0.0.1) 439.21ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:53:26.114 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:53:26.439 503 GET /script-health-check (127.0.0.1) 465.66ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:53:31.123 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:53:31.441 503 GET /script-health-check (127.0.0.1) 459.11ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:53:36.042 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:53:36.411 503 GET /script-health-check (127.0.0.1) 461.51ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:53:41.113 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:53:41.472 503 GET /script-health-check (127.0.0.1) 496.28ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:53:46.139 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:53:46.495 503 GET /script-health-check (127.0.0.1) 496.78ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:53:51.055 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:53:51.430 503 GET /script-health-check (127.0.0.1) 463.24ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:53:56.116 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:53:56.463 503 GET /script-health-check (127.0.0.1) 477.79ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:54:01.074 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:54:01.408 503 GET /script-health-check (127.0.0.1) 463.00ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:54:06.109 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:54:06.441 503 GET /script-health-check (127.0.0.1) 468.86ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:54:11.125 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:54:11.479 503 GET /script-health-check (127.0.0.1) 495.87ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:54:16.100 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:54:16.474 503 GET /script-health-check (127.0.0.1) 486.05ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:54:21.071 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:54:21.422 503 GET /script-health-check (127.0.0.1) 439.19ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:54:26.121 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:54:26.453 503 GET /script-health-check (127.0.0.1) 469.31ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:54:31.091 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:54:31.448 503 GET /script-health-check (127.0.0.1) 453.55ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:54:36.078 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:54:36.424 503 GET /script-health-check (127.0.0.1) 454.91ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:54:41.103 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:54:41.487 503 GET /script-health-check (127.0.0.1) 523.28ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:54:46.127 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:54:46.493 503 GET /script-health-check (127.0.0.1) 492.83ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:54:51.089 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:54:51.430 503 GET /script-health-check (127.0.0.1) 441.32ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:54:56.121 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:54:56.452 503 GET /script-health-check (127.0.0.1) 468.53ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:55:01.091 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:55:01.423 503 GET /script-health-check (127.0.0.1) 465.85ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:55:06.111 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:55:06.438 503 GET /script-health-check (127.0.0.1) 461.32ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:55:11.116 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:55:11.420 503 GET /script-health-check (127.0.0.1) 425.80ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:55:16.100 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:55:16.431 503 GET /script-health-check (127.0.0.1) 441.60ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:55:21.102 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:55:21.459 503 GET /script-health-check (127.0.0.1) 498.17ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:55:26.060 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:55:26.409 503 GET /script-health-check (127.0.0.1) 445.18ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:55:31.087 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:55:31.431 503 GET /script-health-check (127.0.0.1) 428.97ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:55:36.101 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:55:36.429 503 GET /script-health-check (127.0.0.1) 467.12ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:55:41.096 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:55:41.453 503 GET /script-health-check (127.0.0.1) 495.29ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:55:46.047 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:55:46.400 503 GET /script-health-check (127.0.0.1) 444.38ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:55:51.079 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:55:51.412 503 GET /script-health-check (127.0.0.1) 423.97ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:55:56.106 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:55:56.463 503 GET /script-health-check (127.0.0.1) 499.16ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:56:01.140 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:56:01.490 503 GET /script-health-check (127.0.0.1) 489.26ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:56:06.121 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:56:06.458 503 GET /script-health-check (127.0.0.1) 466.15ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:56:11.140 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:56:11.499 503 GET /script-health-check (127.0.0.1) 502.12ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:56:16.053 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:56:16.385 503 GET /script-health-check (127.0.0.1) 427.07ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:56:21.063 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:56:21.432 503 GET /script-health-check (127.0.0.1) 505.92ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:56:26.122 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:56:26.454 503 GET /script-health-check (127.0.0.1) 472.22ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:56:31.089 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:56:31.438 503 GET /script-health-check (127.0.0.1) 455.01ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:56:36.051 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:56:36.392 503 GET /script-health-check (127.0.0.1) 472.91ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:56:41.083 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:56:41.474 503 GET /script-health-check (127.0.0.1) 525.67ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:56:46.091 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:56:46.453 503 GET /script-health-check (127.0.0.1) 506.52ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:56:51.107 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:56:51.437 503 GET /script-health-check (127.0.0.1) 462.30ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:56:56.075 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:56:56.402 503 GET /script-health-check (127.0.0.1) 430.95ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:57:01.037 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:57:01.404 503 GET /script-health-check (127.0.0.1) 493.26ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:57:06.068 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:57:06.404 503 GET /script-health-check (127.0.0.1) 443.87ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:57:11.144 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:57:11.495 503 GET /script-health-check (127.0.0.1) 483.07ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:57:16.058 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:57:16.400 503 GET /script-health-check (127.0.0.1) 435.05ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:57:21.101 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:57:21.453 503 GET /script-health-check (127.0.0.1) 490.95ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:57:26.090 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:57:26.446 503 GET /script-health-check (127.0.0.1) 492.74ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:57:31.121 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:57:31.459 503 GET /script-health-check (127.0.0.1) 480.40ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:57:36.061 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:57:36.425 503 GET /script-health-check (127.0.0.1) 449.52ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:57:41.129 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:57:41.489 503 GET /script-health-check (127.0.0.1) 492.72ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:57:46.085 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:57:46.429 503 GET /script-health-check (127.0.0.1) 459.11ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:57:51.117 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:57:51.479 503 GET /script-health-check (127.0.0.1) 499.50ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:57:56.098 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:57:56.461 503 GET /script-health-check (127.0.0.1) 501.17ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:58:01.052 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:58:01.389 503 GET /script-health-check (127.0.0.1) 426.68ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:58:06.117 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:58:06.455 503 GET /script-health-check (127.0.0.1) 469.99ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:58:11.133 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:58:11.524 503 GET /script-health-check (127.0.0.1) 513.67ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:58:16.118 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:58:16.459 503 GET /script-health-check (127.0.0.1) 473.69ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:58:21.090 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:58:21.445 503 GET /script-health-check (127.0.0.1) 495.16ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:58:26.126 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:58:26.456 503 GET /script-health-check (127.0.0.1) 466.94ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:58:31.065 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:58:31.416 503 GET /script-health-check (127.0.0.1) 443.39ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:58:36.106 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:58:36.435 503 GET /script-health-check (127.0.0.1) 446.77ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:58:41.127 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:58:41.496 503 GET /script-health-check (127.0.0.1) 505.72ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:58:46.107 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:58:46.469 503 GET /script-health-check (127.0.0.1) 464.74ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:58:51.082 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:58:51.431 503 GET /script-health-check (127.0.0.1) 437.46ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:58:56.102 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:58:56.447 503 GET /script-health-check (127.0.0.1) 464.65ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:59:01.108 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:59:01.436 503 GET /script-health-check (127.0.0.1) 445.85ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:59:06.068 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:59:06.423 503 GET /script-health-check (127.0.0.1) 489.88ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:59:11.089 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:59:11.424 503 GET /script-health-check (127.0.0.1) 443.30ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:59:16.082 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:59:16.446 503 GET /script-health-check (127.0.0.1) 461.83ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:59:21.122 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:59:21.471 503 GET /script-health-check (127.0.0.1) 490.66ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:59:26.068 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:59:26.396 503 GET /script-health-check (127.0.0.1) 416.89ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:59:31.121 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:59:31.486 503 GET /script-health-check (127.0.0.1) 505.22ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:59:36.103 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:59:36.472 503 GET /script-health-check (127.0.0.1) 510.20ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:59:41.101 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:59:41.475 503 GET /script-health-check (127.0.0.1) 489.18ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:59:46.079 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:59:46.421 503 GET /script-health-check (127.0.0.1) 446.03ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:59:51.137 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:59:51.490 503 GET /script-health-check (127.0.0.1) 500.64ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 13:59:56.064 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 13:59:56.397 503 GET /script-health-check (127.0.0.1) 470.65ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:00:01.096 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:00:01.440 503 GET /script-health-check (127.0.0.1) 441.81ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:00:06.121 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:00:06.459 503 GET /script-health-check (127.0.0.1) 477.73ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:00:11.132 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:00:11.479 503 GET /script-health-check (127.0.0.1) 486.20ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:00:16.104 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:00:16.443 503 GET /script-health-check (127.0.0.1) 477.19ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:00:21.080 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:00:21.406 503 GET /script-health-check (127.0.0.1) 427.90ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:00:26.102 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:00:26.459 503 GET /script-health-check (127.0.0.1) 459.68ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:00:31.142 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:00:31.501 503 GET /script-health-check (127.0.0.1) 500.12ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:00:36.099 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:00:36.460 503 GET /script-health-check (127.0.0.1) 490.20ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:00:41.140 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:00:41.482 503 GET /script-health-check (127.0.0.1) 485.24ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:00:46.091 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:00:46.448 503 GET /script-health-check (127.0.0.1) 462.35ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:00:51.086 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:00:51.425 503 GET /script-health-check (127.0.0.1) 445.84ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:00:56.142 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:00:56.492 503 GET /script-health-check (127.0.0.1) 488.60ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:01:01.096 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:01:01.447 503 GET /script-health-check (127.0.0.1) 449.61ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:01:06.081 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:01:06.415 503 GET /script-health-check (127.0.0.1) 426.66ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:01:11.114 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:01:11.479 503 GET /script-health-check (127.0.0.1) 477.94ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:01:16.095 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:01:16.433 503 GET /script-health-check (127.0.0.1) 428.41ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:01:21.143 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:01:21.484 503 GET /script-health-check (127.0.0.1) 481.77ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:01:26.129 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:01:26.463 503 GET /script-health-check (127.0.0.1) 467.12ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:01:31.112 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:01:31.462 503 GET /script-health-check (127.0.0.1) 486.58ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:01:36.114 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:01:36.459 503 GET /script-health-check (127.0.0.1) 480.11ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:01:41.029 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:01:41.378 503 GET /script-health-check (127.0.0.1) 440.09ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:01:46.068 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:01:46.399 503 GET /script-health-check (127.0.0.1) 456.81ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:01:51.076 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:01:51.409 503 GET /script-health-check (127.0.0.1) 419.26ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:01:56.066 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:01:56.407 503 GET /script-health-check (127.0.0.1) 473.79ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:02:01.111 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:02:01.489 503 GET /script-health-check (127.0.0.1) 496.29ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:02:06.109 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:02:06.437 503 GET /script-health-check (127.0.0.1) 466.81ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:02:11.116 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:02:11.476 503 GET /script-health-check (127.0.0.1) 477.10ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:02:16.086 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:02:16.417 503 GET /script-health-check (127.0.0.1) 434.79ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:02:21.095 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:02:21.454 503 GET /script-health-check (127.0.0.1) 470.92ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:02:26.132 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:02:26.465 503 GET /script-health-check (127.0.0.1) 445.64ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:02:31.096 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:02:31.455 503 GET /script-health-check (127.0.0.1) 483.83ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:02:36.044 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:02:36.381 503 GET /script-health-check (127.0.0.1) 458.61ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:02:41.086 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:02:41.440 503 GET /script-health-check (127.0.0.1) 494.25ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:02:46.040 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:02:46.401 503 GET /script-health-check (127.0.0.1) 496.92ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:02:51.112 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:02:51.450 503 GET /script-health-check (127.0.0.1) 468.95ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:02:56.124 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:02:56.456 503 GET /script-health-check (127.0.0.1) 470.87ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:03:01.100 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:03:01.446 503 GET /script-health-check (127.0.0.1) 456.10ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:03:06.084 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:03:06.421 503 GET /script-health-check (127.0.0.1) 462.90ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:03:11.135 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:03:11.503 503 GET /script-health-check (127.0.0.1) 503.89ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:03:16.069 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:03:16.407 503 GET /script-health-check (127.0.0.1) 427.39ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:03:21.078 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:03:21.485 503 GET /script-health-check (127.0.0.1) 528.76ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:03:26.107 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:03:26.455 503 GET /script-health-check (127.0.0.1) 486.06ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:03:31.065 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:03:31.393 503 GET /script-health-check (127.0.0.1) 418.28ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:03:36.087 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:03:36.429 503 GET /script-health-check (127.0.0.1) 465.76ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:03:41.095 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:03:41.460 503 GET /script-health-check (127.0.0.1) 454.70ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:03:46.117 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:03:46.459 503 GET /script-health-check (127.0.0.1) 463.41ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:03:51.070 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:03:51.416 503 GET /script-health-check (127.0.0.1) 470.43ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:03:56.102 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:03:56.448 503 GET /script-health-check (127.0.0.1) 443.03ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:04:01.053 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:04:01.429 503 GET /script-health-check (127.0.0.1) 492.39ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:04:06.102 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:04:06.424 503 GET /script-health-check (127.0.0.1) 424.42ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:04:11.098 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:04:11.432 503 GET /script-health-check (127.0.0.1) 441.13ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:04:16.116 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:04:16.462 503 GET /script-health-check (127.0.0.1) 484.81ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:04:21.112 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:04:21.448 503 GET /script-health-check (127.0.0.1) 470.26ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:04:26.091 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:04:26.438 503 GET /script-health-check (127.0.0.1) 485.41ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:04:31.073 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:04:31.436 503 GET /script-health-check (127.0.0.1) 504.46ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:04:36.122 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:04:36.498 503 GET /script-health-check (127.0.0.1) 519.21ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:04:41.089 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:04:41.433 503 GET /script-health-check (127.0.0.1) 441.98ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:04:46.128 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:04:46.487 503 GET /script-health-check (127.0.0.1) 499.44ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:04:51.118 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:04:51.458 503 GET /script-health-check (127.0.0.1) 460.73ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:04:56.095 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:04:56.465 503 GET /script-health-check (127.0.0.1) 508.92ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:05:01.119 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:05:01.445 503 GET /script-health-check (127.0.0.1) 453.75ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:05:06.055 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:05:06.396 503 GET /script-health-check (127.0.0.1) 450.49ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:05:11.108 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:05:11.450 503 GET /script-health-check (127.0.0.1) 459.97ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:05:16.078 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:05:16.406 503 GET /script-health-check (127.0.0.1) 437.24ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:05:21.090 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:05:21.417 503 GET /script-health-check (127.0.0.1) 459.59ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:05:26.137 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:05:26.478 503 GET /script-health-check (127.0.0.1) 482.94ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:05:31.138 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:05:31.502 503 GET /script-health-check (127.0.0.1) 504.09ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:05:36.077 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:05:36.413 503 GET /script-health-check (127.0.0.1) 434.66ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:05:41.081 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:05:41.460 503 GET /script-health-check (127.0.0.1) 479.57ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:05:46.130 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:05:46.479 503 GET /script-health-check (127.0.0.1) 485.39ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:05:51.077 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:05:51.433 503 GET /script-health-check (127.0.0.1) 446.41ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:05:56.058 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:05:56.418 503 GET /script-health-check (127.0.0.1) 447.58ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:06:01.030 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:06:01.397 503 GET /script-health-check (127.0.0.1) 464.80ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:56 in <module>          

                                                                                

     53 model = load_model()                                                    

     54                                                                         

     55 # Initialize expected values                                            

  ❱  56 df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation  

     57                                                                         

     58 # Tab layout                                                            

     59 tabs = st.tabs(['Rate Change', 'Actual vs Expected', 'Shapley Values']  

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py:1010    

  in predict                                                                    

                                                                                

    1007 │   │   │   X = _LGBMCheckArray(X, accept_sparse=True, force_all_fini  

    1008 │   │   n_features = X.shape[1]                                        

    1009 │   │   if self._n_features != n_features:                             

  ❱ 1010 │   │   │   raise ValueError(                                          

    1011 │   │   │   │   "Number of features of the model must "                

    1012 │   │   │   │   f"match the input. Model n_features_ is {self._n_feat  

    1013 │   │   │   │   f"input n_features is {n_features}"                    

────────────────────────────────────────────────────────────────────────────────

ValueError: Number of features of the model must match the input. Model 

n_features_ is 11 and input n_features is 20

2025-02-04 14:06:06.079 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 56, in <module>

    df['Expected'] = model.predict(pd.get_dummies(df, columns=["Occupation_v4", "Region_bnd"], drop_first=True))

                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/lightgbm/sklearn.py", line 1010, in predict

    raise ValueError(

ValueError: Number of features of the model must match the input. Model n_features_ is 11 and input n_features is 20

2025-02-04 14:06:06.416 503 GET /script-health-check (127.0.0.1) 438.14ms

[14:06:10] 🐙 Pulling code changes from Github...

[14:06:10] 📦 Processing dependencies...

[14:06:10] 📦 Processed dependencies!

2025-02-04 14:06:13.519 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:06:13.776 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


[14:06:14] 🔄 Updated app!

2025-02-04 14:06:17.217 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:06:24.028 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:08:42.548 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:13:42.543 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:14:12.883 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:14:17.208 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:18:42.552 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


[14:19:51] 🐙 Pulling code changes from Github...

[14:19:51] 📦 Processing dependencies...

[14:19:51] 📦 Processed dependencies!

2025-02-04 14:19:53.728 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


[14:19:53] 🔄 Updated app!

2025-02-04 14:20:07.039 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:20:11.750 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:22:51.827 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:23:42.223 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


[14:28:25] 🐙 Pulling code changes from Github...

[14:28:26] 📦 Processing dependencies...

[14:28:26] 📦 Processed dependencies!

2025-02-04 14:28:27.768 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


[14:28:28] 🔄 Updated app!

2025-02-04 14:28:42.460 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:31:06.807 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:31:12.322 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


[14:31:14] 🐙 Pulling code changes from Github...

[14:31:14] 📦 Processing dependencies...

[14:31:14] 📦 Processed dependencies!

[14:31:16] 🔄 Updated app!

2025-02-04 14:31:27.131 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:33:42.467 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:38:43.044 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:43:42.346 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


[14:46:57] 🐙 Pulling code changes from Github...

[14:46:58] 📦 Processing dependencies...

[14:46:58] 📦 Processed dependencies!

2025-02-04 14:46:59.463 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


[14:46:59] 🔄 Updated app!

2025-02-04 14:47:16.901 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:47:21.596 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:47:24.550 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:47:27.266 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:47:34.039 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:47:37.082 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:47:38.799 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:47:48.984 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:47:57.378 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:48:42.316 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:53:42.908 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 14:58:42.594 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


2025-02-04 15:03:42.427 

Calling `st.pyplot()` without providing a figure argument has been deprecated

and will be removed in a later version as it requires the use of Matplotlib's

global figure object, which is not thread-safe.


To future-proof this code, you should pass in a figure as shown below:


```python

fig, ax = plt.subplots()

ax.scatter([1, 2, 3], [1, 2, 3])

# other plotting actions...

st.pyplot(fig)

```


If you have a specific use case that requires this functionality, please let us

know via [issue on Github](https://github.com/streamlit/streamlit/issues).


[15:06:06] 🐙 Pulling code changes from Github...

[15:06:06] 📦 Processing dependencies...

[15:06:06] 📦 Processed dependencies!

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/pandas/core/indexes/base.p  

  y:3805 in get_loc                                                             

                                                                                

    3802 │   │   """                                                            

    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3804 │   │   try:                                                           

  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    

    3806 │   │   except KeyError as err:                                        

    3807 │   │   │   if isinstance(casted_key, slice) or (                      

    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Region'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:121 in <module>         

                                                                                

    118 │                                                                       

    119 │   # Actual values as bars (Y-axis 1)                                  

    120 │   fig.add_trace(go.Bar(                                               

  ❱ 121 │   │   x=exposure_summary[factor],                                     

    122 │   │   y=exposure_summary["Actual"],                                   

    123 │   │   name='Actual',                                                  

    124 │   │   marker_color='green',                                           

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/pandas/core/frame.py:4102   

  in __getitem__                                                                

                                                                                

     4099 │   │   if is_single_key:                                             

     4100 │   │   │   if self.columns.nlevels > 1:                              

     4101 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4102 │   │   │   indexer = self.columns.get_loc(key)                       

     4103 │   │   │   if is_integer(indexer):                                   

     4104 │   │   │   │   indexer = [indexer]                                   

     4105 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3810 │   │   │   ):                                                         

    3811 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3812 │   │   │   raise KeyError(key) from err                               

    3813 │   │   except TypeError:                                              

    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Region'

2025-02-04 15:06:08.057 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/pandas/core/indexes/base.py", line 3805, in get_loc

    return self._engine.get_loc(casted_key)

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc

  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc

  File "pandas/_libs/hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item

  File "pandas/_libs/hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item

KeyError: 'Region'


The above exception was the direct cause of the following exception:


Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 121, in <module>

    x=exposure_summary[factor],

      ~~~~~~~~~~~~~~~~^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/pandas/core/frame.py", line 4102, in __getitem__

    indexer = self.columns.get_loc(key)

              ^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/pandas/core/indexes/base.py", line 3812, in get_loc

    raise KeyError(key) from err

KeyError: 'Region'

[15:06:08] 🔄 Updated app!

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/pandas/core/indexes/base.p  

  y:3805 in get_loc                                                             

                                                                                

    3802 │   │   """                                                            

    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3804 │   │   try:                                                           

  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    

    3806 │   │   except KeyError as err:                                        

    3807 │   │   │   if isinstance(casted_key, slice) or (                      

    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Region'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/alex-optimisation-demo/rate_change_test.py:121 in <module>         

                                                                                

    118 │                                                                       

    119 │   # Actual values as bars (Y-axis 1)                                  

    120 │   fig.add_trace(go.Bar(                                               

  ❱ 121 │   │   x=exposure_summary[factor],                                     

    122 │   │   y=exposure_summary["Actual"],                                   

    123 │   │   name='Actual',                                                  

    124 │   │   marker_color='green',                                           

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/pandas/core/frame.py:4102   

  in __getitem__                                                                

                                                                                

     4099 │   │   if is_single_key:                                             

     4100 │   │   │   if self.columns.nlevels > 1:                              

     4101 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4102 │   │   │   indexer = self.columns.get_loc(key)                       

     4103 │   │   │   if is_integer(indexer):                                   

     4104 │   │   │   │   indexer = [indexer]                                   

     4105 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.12/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3810 │   │   │   ):                                                         

    3811 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3812 │   │   │   raise KeyError(key) from err                               

    3813 │   │   except TypeError:                                              

    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Region'

2025-02-04 15:06:23.815 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/pandas/core/indexes/base.py", line 3805, in get_loc

    return self._engine.get_loc(casted_key)

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc

  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc

  File "pandas/_libs/hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item

  File "pandas/_libs/hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item

KeyError: 'Region'


The above exception was the direct cause of the following exception:


Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling

    result = func()

             ^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec

    exec(code, module.__dict__)

  File "/mount/src/alex-optimisation-demo/rate_change_test.py", line 121, in <module>

    x=exposure_summary[factor],

      ~~~~~~~~~~~~~~~~^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/pandas/core/frame.py", line 4102, in __getitem__

    indexer = self.columns.get_loc(key)

              ^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/adminuser/venv/lib/python3.12/site-packages/pandas/core/indexes/base.py", line 3812, in get_loc

    raise KeyError(key) from err

KeyError: 'Region'
