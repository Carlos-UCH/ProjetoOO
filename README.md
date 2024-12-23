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

<p>1. Edit the main.py file and add your equations:</p>

<h4>First degree equation</h4>

ax + b = 0


~~~
#3x - 6 = 0
eq1 = EqPrimeiroGrau(3, -6)  
~~~


<h4>Quadratic Equation</h4>

ax^2+bx+c=0 


~~~
#x^2 - 2x - 3 = 0
eq2 = EqSegundoGrau(1, -2, -3) 
~~~

<h4>Cubic equation</h4>

ax^3+bx^2+cx+d=0

~~~
#x^3 - 4x^2 + 6x - 3 = 0
eq3 = EqTerceiroGrau(1, -4, 6, -3) 

~~~

<p>2. Run the main.py file:</p> 

~~~
python3 main.py
~~~


<p>3. Running the system</p> 

~~~
0. *CASO FECHOU O PROGRAMA (CARREGAR)*
~~~
All data will be loaded from json to the current file, synchronizing previous results

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
============================================================================================

<b>All generated graphs are in </b> /graficos <b>and the total report with results, coefficients and graphs are in</b> /graficos/resultados

============================================================================================