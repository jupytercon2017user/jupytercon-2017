
morphology = '''
<center>
<style>
    .un {
    background-color:'red';
    }
    .reach {
    background-color:'green';
    }
    .able {
    background-color:'blue';
    }
</style>
<h3>Morphology</h3>
<h5>'<span class='un'>Un</span><span class='reach'>reach</span><span class='able'>able</span>\'</h5>
<br>
<table border="1" class="dataframe">
<thead>\n    
<tr style="text-align: right;">
<th></th>
<th>Effect</th>
<th>Morpheme</th>
</tr>\n    <tr>\n      <th></th>\n      <th></th>\n      <th></th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>un</th>\n      <td>Negation</td>\n      <td>Prefix</td>\n    </tr>\n    <tr>\n      <th>reach</th>\n      <td>Verb</td>\n      <td>Root</td>\n    </tr>\n    <tr>\n      <th>able</th>\n      <td>To Adjective</td>\n      <td>Suffix</td>\n    </tr>\n  </tbody>\n</table>'
</center>
'''


syntax = """
<center>
<h3> Syntax </h3>
<br>
<h5> Exchangeability within syntactic classes. </h5>
<br>
<br>
<svg class="displacy" width="950" height="220" viewBox="0 0 950 220" preserveAspectRatio="xMinYMax meet" data-format="spacy" id="displacy-svg" style="color: rgb(245, 244, 240); background: rgb(39, 40, 34); font-family: inherit;">

	<text class="displacy-token" fill="currentColor" data-tag="PRP" text-anchor="middle" y="140">
		<tspan class="displacy-word" x="300" fill="currentColor" data-tag="PRP">He</tspan>

	</text>

	<text class="displacy-token" fill="currentColor" data-tag="VBD" text-anchor="middle" y="140">
		<tspan class="displacy-word" x="340" fill="currentColor" data-tag="VBD">went</tspan>

	</text>
	<text class="displacy-token" fill="currentColor" data-tag="VBD" text-anchor="middle" y="140">
		<tspan class="displacy-word" x="380" fill="currentColor" data-tag="VBD">to</tspan>

	</text>

		<text class="displacy-token" fill="currentColor" data-tag="VBD" text-anchor="middle" y="140">
		<tspan class="displacy-word" x="420" fill="currentColor" data-tag="VBD">the</tspan>

	</text>

		<text class="displacy-token" fill="currentColor" data-tag="VBD" text-anchor="middle" y="140">
		<tspan class="displacy-word" x="460" fill="currentColor" data-tag="VBD">store.</tspan>

	</text>




		<text class="displacy-token" fill="currentColor" data-tag="VBD" text-anchor="middle" y="140">
		<tspan class="displacy-word" x="50" fill="currentColor" data-tag="VBD">She</tspan>
		<tspan class="displacy-word" x="50" fill="currentColor" dy="1em" data-tag="VBD">John</tspan>
		<tspan class="displacy-word" x="50" fill="currentColor" dy="1em" data-tag="VBD">The man</tspan>


	</text>






	<g class="displacy-arrow" data-dir="left" data-label="nsubj">
		<path class="displacy-arc" d="M50,100 C150,0 300,0 300,100" stroke-width="2px" fill="none" stroke="currentColor" data-dir="left" data-label="nsubj" id="arrow-0"></path>
		<text dy="1em">
			<textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="nsubj" data-dir="left" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-0">Exchangeable subjects</textPath>
		</text>
		<path class="displacy-arrowhead" d="M300,102 L294,92 306,92" fill="currentColor" data-label="nsubj" data-dir="left"></path>
	</g>

</svg>

<br>
<br>
<h5>Compiling Syntactic Units</h5>
<br>

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg .tg-yw4l{vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-yw4l">The</th>
    <th class="tg-yw4l">man</th>
    <th class="tg-yw4l">went</th>
    <th class="tg-yw4l">to </th>
    <th class="tg-yw4l">the</th>
    <th class="tg-yw4l">store</th>
  </tr>
  <tr>
    <td class="tg-yw4l">determiner</td>
    <td class="tg-yw4l">simple subject</td>
    <td class="tg-yw4l">verb</td>
    <td class="tg-yw4l">preposition<br></td>
    <td class="tg-yw4l">determiner</td>
    <td class="tg-yw4l">object (of preposition)</td>
  </tr>
  <tr>
    <td class="tg-yw4l" colspan="2">subject phrase</td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l" colspan="3">prepositional phrase</td>
  </tr>
  <tr>
    <td class="tg-yw4l" colspan="2"></td>
    <td class="tg-yw4l" colspan="4">verb phrase</td>
  </tr>
</table>
</center>
"""


elephant1 = """

<svg class="displacy" width="1550" height="320" viewBox="0 0 1550 320" preserveAspectRatio="xMinYMax meet" data-format="spacy" id="displacy-svg" style="color: rgb(245, 244, 240); background: rgb(39, 40, 34); font-family: inherit;">

	<text class="displacy-token" fill="currentColor" data-tag="DT" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="150" fill="currentColor" data-tag="DT">This
		</tspan>

		<tspan class="displacy-tag" x="150" dy="2em" fill="currentColor" data-tag="DT">DT
		</tspan>
	</text>

	<text class="displacy-token" fill="currentColor" data-tag="NN" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="350" fill="currentColor" data-tag="NN">morning</tspan>

		<tspan class="displacy-tag" x="350" dy="2em" fill="currentColor" data-tag="NN">NN</tspan>

	</text>

	<text class="displacy-token" fill="currentColor" data-tag="PRP" text-anchor="middle" y="240">

		<tspan class="displacy-word" x="550" fill="currentColor" data-tag="PRP">I</tspan>

		<tspan class="displacy-tag" x="550" dy="2em" fill="currentColor" data-tag="PRP">PRP</tspan>

	</text>
	<text class="displacy-token" fill="currentColor" data-tag="VBD" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="750" fill="currentColor" data-tag="VBD">shot</tspan>

		<tspan class="displacy-tag" x="750" dy="2em" fill="currentColor" data-tag="VBD">VBD</tspan>
	</text>

	<text class="displacy-token" fill="currentColor" data-tag="NN" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="950" fill="currentColor" data-tag="NN">an elephant</tspan>

		<tspan class="displacy-tag" x="950" dy="2em" fill="currentColor" data-tag="NN">NN</tspan>
	</text>

	<text class="displacy-token" fill="currentColor" data-tag="IN" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="1150" fill="currentColor" data-tag="IN">in</tspan>

		<tspan class="displacy-tag" x="1150" dy="2em" fill="currentColor" data-tag="IN">IN</tspan>
	</text>

	<text class="displacy-token" fill="currentColor" data-tag="NNS" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="1350" fill="currentColor" data-tag="NNS">my pajamas</tspan>

		<tspan class="displacy-tag" x="1350" dy="2em" fill="currentColor" data-tag="NNS">NNS</tspan></text><g class="displacy-arrow" data-dir="left" data-label="det">

<!--
	<path class="displacy-arc" d="M152.5,200 C152.5,100 347.5,100 347.5,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="left" data-label="det" id="arrow-0"></path>
	<text dy="1em">
	<textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="det" data-dir="left" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-0">det</textPath>
	</text>
	<path class="displacy-arrowhead" d="M152.5,202 L146.5,192 158.5,192" fill="currentColor" data-label="det" data-dir="left"></path></g>
	<g class="displacy-arrow" data-dir="left" data-label="npadvmod"><path class="displacy-arc" d="M350,200 C350,0 750,0 750,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="left" data-label="npadvmod" id="arrow-1"></path><text dy="1em">
	<textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="npadvmod" data-dir="left" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-1">npadvmod</textPath></text><path class="displacy-arrowhead" d="M350,202 L344,192 356,192" fill="currentColor" data-label="npadvmod" data-dir="left"></path></g><g class="displacy-arrow" data-dir="left" data-label="nsubj"><path class="displacy-arc" d="M552.5,200 C552.5,100 747.5,100 747.5,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="left" data-label="nsubj" id="arrow-2"></path><text dy="1em"><textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="nsubj" data-dir="left" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-2">nsubj</textPath></text>
	<path class="displacy-arrowhead" d="M552.5,202 L546.5,192 558.5,192" fill="currentColor" data-label="nsubj" data-dir="left"></path></g>
-->
	<g class="displacy-arrow" data-dir="right" data-label="dobj"><path class="displacy-arc" d="M752.5,200 C752.5,100 947.5,100 947.5,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="right" data-label="dobj" id="arrow-3"></path><text dy="1em"><textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="dobj" data-dir="right" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-3">dobj</textPath></text><path class="displacy-arrowhead" d="M947.5,202 L953.5,192 941.5,192" fill="currentColor" data-label="dobj" data-dir="right"></path></g><g class="displacy-arrow" data-dir="right" data-label="prep"><path class="displacy-arc" d="M750,200 C750,0 1150,0 1150,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="right" data-label="prep" id="arrow-4"></path><text dy="1em">

	<textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="prep" data-dir="right" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-4">prep</textPath></text><path class="displacy-arrowhead" d="M1150,202 L1156,192 1144,192" fill="currentColor" data-label="prep" data-dir="right"></path></g><g class="displacy-arrow" data-dir="right" data-label="pobj"><path class="displacy-arc" d="M1152.5,200 C1152.5,100 1347.5,100 1347.5,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="right" data-label="pobj" id="arrow-5"></path><text dy="1em"><textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="pobj" data-dir="right" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-5">pobj</textPath></text><path class="displacy-arrowhead" d="M1347.5,202 L1353.5,192 1341.5,192" fill="currentColor" data-label="pobj" data-dir="right"></path></g>

	</svg>
"""


elephant2 = """
<svg class="displacy" width="1550" height="320" viewBox="0 0 1550 320" preserveAspectRatio="xMinYMax meet" data-format="spacy" id="displacy-svg" style="color: rgb(245, 244, 240); background: rgb(39, 40, 34); font-family: inherit;">

	<text class="displacy-token" fill="currentColor" data-tag="DT" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="150" fill="currentColor" data-tag="DT">This
		</tspan>

		<tspan class="displacy-tag" x="150" dy="2em" fill="currentColor" data-tag="DT">DT
		</tspan>
	</text>

	<text class="displacy-token" fill="currentColor" data-tag="NN" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="350" fill="currentColor" data-tag="NN">morning</tspan>

		<tspan class="displacy-tag" x="350" dy="2em" fill="currentColor" data-tag="NN">NN</tspan>

	</text>

	<text class="displacy-token" fill="currentColor" data-tag="PRP" text-anchor="middle" y="240">

		<tspan class="displacy-word" x="550" fill="currentColor" data-tag="PRP">I</tspan>

		<tspan class="displacy-tag" x="550" dy="2em" fill="currentColor" data-tag="PRP">PRP</tspan>

	</text>
	<text class="displacy-token" fill="currentColor" data-tag="VBD" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="750" fill="currentColor" data-tag="VBD">shot</tspan>

		<tspan class="displacy-tag" x="750" dy="2em" fill="currentColor" data-tag="VBD">VBD</tspan>
	</text>

	<text class="displacy-token" fill="currentColor" data-tag="NN" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="950" fill="currentColor" data-tag="NN">an elephant</tspan>

		<tspan class="displacy-tag" x="950" dy="2em" fill="currentColor" data-tag="NN">NN</tspan>
	</text>

	<text class="displacy-token" fill="currentColor" data-tag="IN" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="1150" fill="currentColor" data-tag="IN">in</tspan>

		<tspan class="displacy-tag" x="1150" dy="2em" fill="currentColor" data-tag="IN">IN</tspan>
	</text>

	<text class="displacy-token" fill="currentColor" data-tag="NNS" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="1350" fill="currentColor" data-tag="NNS">my pajamas</tspan>

		<tspan class="displacy-tag" x="1350" dy="2em" fill="currentColor" data-tag="NNS">NNS</tspan></text><g class="displacy-arrow" data-dir="left" data-label="det">

<!--
	<path class="displacy-arc" d="M152.5,200 C152.5,100 347.5,100 347.5,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="left" data-label="det" id="arrow-0"></path>
	<text dy="1em">
	<textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="det" data-dir="left" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-0">det</textPath>
	</text>
	<path class="displacy-arrowhead" d="M152.5,202 L146.5,192 158.5,192" fill="currentColor" data-label="det" data-dir="left"></path></g>
	<g class="displacy-arrow" data-dir="left" data-label="npadvmod"><path class="displacy-arc" d="M350,200 C350,0 750,0 750,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="left" data-label="npadvmod" id="arrow-1"></path><text dy="1em">
	<textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="npadvmod" data-dir="left" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-1">npadvmod</textPath></text><path class="displacy-arrowhead" d="M350,202 L344,192 356,192" fill="currentColor" data-label="npadvmod" data-dir="left"></path></g><g class="displacy-arrow" data-dir="left" data-label="nsubj"><path class="displacy-arc" d="M552.5,200 C552.5,100 747.5,100 747.5,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="left" data-label="nsubj" id="arrow-2"></path><text dy="1em"><textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="nsubj" data-dir="left" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-2">nsubj</textPath></text>
	<path class="displacy-arrowhead" d="M552.5,202 L546.5,192 558.5,192" fill="currentColor" data-label="nsubj" data-dir="left"></path></g>
-->
	<g class="displacy-arrow" data-dir="right" data-label="dobj"><path class="displacy-arc" d="M752.5,200 C752.5,100 947.5,100 947.5,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="right" data-label="dobj" id="arrow-3"></path>
		<text dy="1em">
			<textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="dobj" data-dir="right" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-3">dobj</textPath>
		</text>

		<path class="displacy-arrowhead" d="M947.5,202 L953.5,192 941.5,192" fill="currentColor" data-label="dobj" data-dir="right"></path></g>


	<g class="displacy-arrow" data-dir="right" data-label="prep"><path class="displacy-arc" d="M947.5,200 C947.5,100 1150,100 1150,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="right" data-label="prep" id="arrow-4"></path>


		<text dy="1em">
			<textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="prep" data-dir="right" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-4">prep</textPath>
		</text>


		<path class="displacy-arrowhead" d="M1150,202 L1156,192 1144,192" fill="currentColor" data-label="prep" data-dir="right"></path></g>


	<g class="displacy-arrow" data-dir="right" data-label="pobj"><path class="displacy-arc" d="M1152.5,200 C1152.5,100 1347.5,100 1347.5,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="right" data-label="pobj" id="arrow-5"></path><text dy="1em"><textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="pobj" data-dir="right" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-5">pobj</textPath></text><path class="displacy-arrowhead" d="M1347.5,202 L1353.5,192 1341.5,192" fill="currentColor" data-label="pobj" data-dir="right"></path></g>

	</svg>
"""


elephant3 = """
<svg class="displacy" width="1550" height="320" viewBox="0 0 1550 320" preserveAspectRatio="xMinYMax meet" data-format="spacy" id="displacy-svg" style="color: rgb(245, 244, 240); background: rgb(39, 40, 34); font-family: inherit;">

	<text class="displacy-token" fill="currentColor" data-tag="DT" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="150" fill="currentColor" data-tag="DT">This
		</tspan>

		<tspan class="displacy-tag" x="150" dy="2em" fill="currentColor" data-tag="DT">DT
		</tspan>
	</text>

	<text class="displacy-token" fill="currentColor" data-tag="NN" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="350" fill="currentColor" data-tag="NN">morning</tspan>

		<tspan class="displacy-tag" x="350" dy="2em" fill="currentColor" data-tag="NN">NN</tspan>

	</text>

	<text class="displacy-token" fill="currentColor" data-tag="PRP" text-anchor="middle" y="240">

		<tspan class="displacy-word" x="550" fill="currentColor" data-tag="PRP">I</tspan>

		<tspan class="displacy-tag" x="550" dy="2em" fill="currentColor" data-tag="PRP">PRP</tspan>

	</text>
	<text class="displacy-token" fill="currentColor" data-tag="VBD" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="750" fill="currentColor" data-tag="VBD">shot</tspan>

		<tspan class="displacy-tag" x="750" dy="2em" fill="currentColor" data-tag="VBD">VBD</tspan>
	</text>

	<text class="displacy-token" fill="currentColor" data-tag="NN" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="950" fill="currentColor" data-tag="NN">an elephant</tspan>

		<tspan class="displacy-tag" x="950" dy="2em" fill="currentColor" data-tag="NN">NN</tspan>
	</text>

	<text class="displacy-token" fill="currentColor" data-tag="IN" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="1150" fill="currentColor" data-tag="IN">in</tspan>

		<tspan class="displacy-tag" x="1150" dy="2em" fill="currentColor" data-tag="IN">IN</tspan>
	</text>

	<text class="displacy-token" fill="currentColor" data-tag="NNS" text-anchor="middle" y="240">
		<tspan class="displacy-word" x="1350" fill="currentColor" data-tag="NNS">my pajamas</tspan>

		<tspan class="displacy-tag" x="1350" dy="2em" fill="currentColor" data-tag="NNS">NNS</tspan></text><g class="displacy-arrow" data-dir="left" data-label="det">

<!--
	<path class="displacy-arc" d="M152.5,200 C152.5,100 347.5,100 347.5,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="left" data-label="det" id="arrow-0"></path>
	<text dy="1em">
	<textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="det" data-dir="left" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-0">det</textPath>
	</text>
	<path class="displacy-arrowhead" d="M152.5,202 L146.5,192 158.5,192" fill="currentColor" data-label="det" data-dir="left"></path></g>
	<g class="displacy-arrow" data-dir="left" data-label="npadvmod"><path class="displacy-arc" d="M350,200 C350,0 750,0 750,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="left" data-label="npadvmod" id="arrow-1"></path><text dy="1em">
	<textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="npadvmod" data-dir="left" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-1">npadvmod</textPath></text><path class="displacy-arrowhead" d="M350,202 L344,192 356,192" fill="currentColor" data-label="npadvmod" data-dir="left"></path></g><g class="displacy-arrow" data-dir="left" data-label="nsubj"><path class="displacy-arc" d="M552.5,200 C552.5,100 747.5,100 747.5,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="left" data-label="nsubj" id="arrow-2"></path><text dy="1em"><textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="nsubj" data-dir="left" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-2">nsubj</textPath></text>
	<path class="displacy-arrowhead" d="M552.5,202 L546.5,192 558.5,192" fill="currentColor" data-label="nsubj" data-dir="left"></path></g>
-->
	<g class="displacy-arrow" data-dir="right" data-label="dobj"><path class="displacy-arc" d="M752.5,200 C752.5,100 947.5,100 947.5,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="right" data-label="dobj" id="arrow-3"></path><text dy="1em"><textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="dobj" data-dir="right" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-3">dobj</textPath></text><path class="displacy-arrowhead" d="M947.5,202 L953.5,192 941.5,192" fill="currentColor" data-label="dobj" data-dir="right"></path></g><g class="displacy-arrow" data-dir="right" data-label="prep"><path class="displacy-arc" d="M947.5,200 C947.5,100 1150,100 1150,200"   stroke-width="2px" fill="none" stroke="currentColor" data-dir="right" data-label="prep" id="arrow-51"></path><text dy="1em">

	<textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="prep" data-dir="right" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-51">prep</textPath>



</text><path class="displacy-arrowhead" d="M1150,202 L1156,192 1144,192" fill="currentColor" data-label="prep" data-dir="right"></path></g><g class="displacy-arrow" data-dir="right" data-label="pobj"><path class="displacy-arc" d="M1152.5,200 C1152.5,100 1347.5,100 1347.5,200" stroke-width="2px" fill="none" stroke="currentColor" data-dir="right" data-label="pobj" id="arrow-5"></path><text dy="1em"><textPath class="displacy-label" startOffset="50%" fill="currentColor" text-anchor="middle" data-label="pobj" data-dir="right" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-5">pobj</textPath></text><path class="displacy-arrowhead" d="M1347.5,202 L1353.5,192 1341.5,192" fill="currentColor" data-label="pobj" data-dir="right"></path></g>

	</svg>
"""


morph_and_syntax = """

<center>
<h3> The importance of Morphology and Syntax:</h3>
<h5> Word order affects semantics:</h5>
<br>

<strong>Original sentence:</strong>
<br>
He did not like the movie, and told the cashier he wanted his money back.
<br>
<br>
<strong>With mutated morpology and word order:</strong>
<br>
The cashier liked the movie, and told him he did not want his money back
<br>
<br>
<br>
<br>
<br>
<br>
<h5> Sometimes only syntax can reveal meaning:</h5>
<br>
Who was wearing the pajamas?
<br>
""" +elephant1+ """
<br>
<br>
""" +elephant3+ """
""" 


valency = """
<center>
<h3>Valency Grammar:</h3></center>

<br>
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> transitive_verb <span style="color: #333333">(</span>subject<span style="color: #008800; font-weight: bold">:</span> <span style="color: #333399; font-weight: bold">noun</span><span style="color: #333333">,</span> object<span style="color: #008800; font-weight: bold">:</span> <span style="color: #333399; font-weight: bold">noun</span><span style="color: #333333">)</span><span style="color: #008800; font-weight: bold">:</span> <span style="color: #333399; font-weight: bold">verb_phrase</span>  <span style="color: #333333">=</span> <span style="color: #333333">{</span>

    <span style="color: #333333">...</span>
<span style="color: #333333">}</span>
</pre></div>

"""

dep_axioms = """
<center>
<h3> Axioms of Dependency Grammar: </h3>
<br>
<h4>1) Each sentence has exactly one root.</h4>
<br>
<object data="assets/axiom1.svg" type="image/svg+xml">
  <img src="assets/axiom1.jpg" />
</object>
<br>
<h4>2) Every word other than the root depends on another element.</h4>
<br>
<object data="assets/singlehead.svg" type="image/svg+xml">
  <img src="assets/singlehead.jpg" width = 50/>
</object>
<br>
<h4>3) No word can depend on more than one element.</h4>
<br>
<object data="assets/non-multi-headed.svg" type="image/svg+xml">
  <img src="assets/non-multi-headed.jpg" width = 50/>
</object>

<br>
<object data="assets/non-multi-headed-normative.svg" type="image/svg+xml">
  <img src="assets/non-multi-headed-normative.jpg" width = 50/>
</object>
<br>
<h4>4) Dependencies do not cross each other (planar trees).</h4>
<br>
<object data="assets/planar-parse.svg" type="image/svg+xml">
  <img src="assets/planar-parse.jpg" width = 50/>
</object>

<br>
<object data="assets/non-planar-parse.svg" type="image/svg+xml">
  <img src="assets/non-planar-parse.jpg" width = 50/>
</object>

</center>"""

cp non-planar-parse.svg ../../tutorial/assets/non-planar-parse.svg
cp planar-parse.s ../../tutorial/assets/

