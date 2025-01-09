# Roots of equations

<p>This is a repository contains a activity carried out in the object-oriented programming course.</p>
<br>

<h2>Installation</h2>

<p> 1. Clone the repository</p>

~~~ 
git clone git@github.com:Carlos-UCH/ProjetoOO.git
~~~ 

<p>2. Install dependencies with pip</p> 

~~~
pip install matplotlib
~~~

~~~
pip install fpdf
~~~

<h2>Usage</h2>

<p>1. Run the main.py file:</p> 

~~~
python3 main.py
~~~


<p>2. Running the system</p> 

~~~
0. *CASO FECHOU O PROGRAMA (CARREGAR)*
~~~
IT IS NECESSARY TO HAVE ALREADY MADE SOME EQUATION AND SAVED IT IN JSON. 

All data will be loaded from json to the current file, synchronizing previous results.

~~~
1. Adicionar Equações
~~~


Each type of equation for finding the root needs to provide the coefficients separated by spaces.

Examples:

<p>1.
(x + 1 = 0)</p>

Write: 1 1

<p>2.
(x^2 - 5x + 6 = 0)</p>

Write: 1 -5 6

<p>3.
(x^3 - 6x^2 + 11x - 6 = 0)</p>


Write: 1 -6 11 -6

~~~
2. Calcular Equações e Gerar PDF
~~~
<b>Report will be generated in</b> /graficos/resultados

~~~
3. Salvar Equações em JSON
~~~
Save equations in JSON
~~~
4. Equações anteriores
~~~
See previous equations and results

~~~
5. Sair
~~~
========================================================================================

<b>All generated graphs are in </b> /graficos <b>and the total report with results, coefficients and graphs are in</b> /graficos/resultados

========================================================================================
