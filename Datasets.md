# Datasets

All ΔΔG datasets in ProDDG were processed to have a unified format. 

ΔΔG values are the folding free energy change of folding (negative values denote stabilization). All datasets obligatorily contain the following data: PDB, Chain, Protein, Gene, Uniprot ID, Uniprot, Organism, Mutation, ΔΔG, Wild-type sequence, Mutant sequence. Wild-type sequence is always provided, there is not a single entry without it, while other protein data may be absent (e.g. if there is no experimental structure available, PDB and Chain will be missing or if the protein is designed de novo, there will be no Uniprot data). If not provided in the original dataset, the wild-type sequence was retrieved from the SEQRES record of PDB structure. Additionally, some datasets may contain information about mutant structures, experimental conditions (pH, T), references, notes, and other information specific to the given dataset. Notes contain comments that were provided with the original dataset. If the entry in the original dataset contains erroneous data it will be stated in the Notes. Mutations have a standard format: < original amino acid >< position >< new amino acid >. Position numbering matches that in the wild-type sequence. If applicable, Mutation PDB is provided with the numbering corresponding to the stated PDB structure.

<table cellspacing="0" border="0">
	<colgroup width="107"></colgroup>
	<colgroup width="193"></colgroup>
	<colgroup width="155"></colgroup>
	<colgroup width="200"></colgroup>
	<colgroup width="310"></colgroup>
	<colgroup width="323"></colgroup>
	<tr>
		<td height="21" align="left" valign=bottom><b><font color="#000000">Columns group</font></b></td>
		<td align="left" valign=bottom><b><font color="#000000">Column name in dataset tsv file</font></b></td>
		<td align="left" valign=bottom><b><font color="#000000">Column name in ProDDG</font></b></td>
		<td align="left" valign=bottom><b><font color="#000000">Column is present in all datasets</font></b></td>
		<td align="left" valign=bottom><b><font color="#000000">Description</font></b></td>
		<td align="left" valign=bottom><b><font color="#000000">How data was derived</font></b></td>
	</tr>
	<tr>
		<td rowspan=7 height="222" align="left" valign=middle><font color="#000000">Main data</font></td>
		<td align="left" valign=bottom><font color="#000000">protein</font></td>
		<td align="left" valign=bottom><font color="#000000">Protein</font></td>
		<td align="left" valign=bottom><font color="#000000">yes</font></td>
		<td align="left" valign=bottom><font color="#000000">Name of the protein studied in the experiment.</font></td>
		<td align="left" valign=bottom><font color="#000000">Protein name as in Uniprot. If Uniprot is not available, the name is derived from header of Fasta file from PDB.</font></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><font color="#000000">mutation</font></td>
		<td align="left" valign=bottom><font color="#000000">Mutation</font></td>
		<td align="left" valign=bottom><font color="#000000">yes</font></td>
		<td align="left" valign=bottom><font color="#000000">Mutation studied in the experiment. Residue numbering corresponds to that in the WT sequence.</font></td>
		<td rowspan=2 align="left" valign=bottom><font color="#000000">As a rule, mutations positions in the original datasets correspond to the numbering in the PDB structure. Firstly, positions were checked for matching the numbering in the stated PDB structure. In case of errors, they were either fixed or documented in &quot;notes&quot; column. Then positions of mutations in sequence were derived from positions in PDB structure.</font></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><font color="#000000">mutation_pdb</font></td>
		<td align="left" valign=bottom><font color="#000000">Mutation (PDB)</font></td>
		<td align="left" valign=bottom><font color="#000000">no</font></td>
		<td align="left" valign=bottom><font color="#000000">Mutation studied in the experiment. Residue numbering corresponds to that in the PDB structure.</font></td>
		</tr>
	<tr>
		<td align="left" valign=bottom><font color="#000000">ddG</font></td>
		<td align="left" valign=bottom><font color="#000000">&Delta;&Delta;G</font></td>
		<td align="left" valign=bottom><font color="#000000">yes</font></td>
		<td align="left" valign=bottom><font color="#000000">Free energy change of folding, kcal/mol. Negative values denote stabilization.</font></td>
		<td align="left" valign=bottom><font color="#000000">Present in the original dataset. If the value is missing, the whole entry was removed.</font></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><font color="#000000">wt_sequence</font></td>
		<td align="left" valign=bottom><font color="#000000">WT sequence</font></td>
		<td align="left" valign=bottom><font color="#000000">yes</font></td>
		<td align="left" valign=bottom><font color="#000000">The sequence of the protein.</font></td>
		<td align="left" valign=bottom><font color="#000000">If no sequence was given in the original dataset, the sequence is derived from the SEQRES of the PDB structure.</font></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><font color="#000000">mutant_sequence</font></td>
		<td align="left" valign=bottom><font color="#000000">Mutant sequence</font></td>
		<td align="left" valign=bottom><font color="#000000">yes</font></td>
		<td align="left" valign=bottom><font color="#000000">Sequence of the mutant.</font></td>
		<td align="left" valign=bottom><font color="#000000">Constructed by introducing mutations to the WT sequence.</font></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><font color="#000000">mutation_context</font></td>
		<td align="left" valign=bottom><font color="#000000">Mutation context</font></td>
		<td align="left" valign=bottom><font color="#000000">yes</font></td>
		<td align="left" valign=bottom><font color="#000000">Mutation context. Mutation that was introduced to the WT protein prior studying the effect of mutation of interest.</font></td>
		<td align="left" valign=bottom><font color="#000000">Present in the original dataset. </font></td>
	</tr>
	<tr>
		<td rowspan=4 height="84" align="left" valign=middle><font color="#000000">Cross-references</font></td>
		<td align="left" valign=bottom><font color="#000000">pdb</font></td>
		<td align="left" valign=bottom><font color="#000000">PDB ID</font></td>
		<td align="left" valign=bottom><font color="#000000">yes</font></td>
		<td align="left" valign=bottom><font color="#000000">PDB ID of the protein structure if available.</font></td>
		<td align="left" valign=bottom><font color="#000000">Present in the original dataset. Was fixed if the original PDB ID became obsolete or is erroneous.</font></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><font color="#000000">chain</font></td>
		<td align="left" valign=bottom><font color="#000000">Chain in PDB structure</font></td>
		<td align="left" valign=bottom><font color="#000000">yes</font></td>
		<td align="left" valign=bottom><font color="#000000">Chain identifier of the protein structure.</font></td>
		<td align="left" valign=bottom><font color="#000000">Present in the original dataset or derived manually from stated PDB ID.</font></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><font color="#000000">uniprot</font></td>
		<td align="left" valign=bottom><font color="#000000">Uniprot</font></td>
		<td align="left" valign=bottom><font color="#000000">yes</font></td>
		<td align="left" valign=bottom><font color="#000000">Uniprot accession number.</font></td>
		<td align="left" valign=bottom><font color="#000000">Derived from stated PDB ID.</font></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000">AlphaFold DB</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000">Protein model in AlphaFold database.</font></td>
		<td align="left" valign=bottom><u><font face="Cambria" color="#0000FF">Derived by adding Uniprot accession number to <a href="https://alphafold.ebi.ac.uk/entry/">https://alphafold.ebi.ac.uk/entry/</a></font></u></td>
	</tr>
	<tr>
		<td height="21" align="left" valign=middle><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000">organism</font></td>
		<td align="left" valign=bottom><font color="#000000">Organism</font></td>
		<td align="left" valign=bottom><font color="#000000">yes</font></td>
		<td align="left" valign=bottom><font color="#000000">Organism</font></td>
		<td align="left" valign=bottom><font color="#000000">Derived from Uniprot if available or header of the PDB structure.</font></td>
	</tr>
	<tr>
		<td height="21" align="left" valign=middle><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000">uniprot_id</font></td>
		<td align="left" valign=bottom><font color="#000000">Uniprot ID</font></td>
		<td align="left" valign=bottom><font color="#000000">yes</font></td>
		<td align="left" valign=bottom><font color="#000000">Uniprot ID</font></td>
		<td align="left" valign=bottom><font color="#000000">Derived from Uniprot.</font></td>
	</tr>
	<tr>
		<td height="21" align="left" valign=middle><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000">gene</font></td>
		<td align="left" valign=bottom><font color="#000000">Gene</font></td>
		<td align="left" valign=bottom><font color="#000000">yes</font></td>
		<td align="left" valign=bottom><font color="#000000">Gene</font></td>
		<td align="left" valign=bottom><font color="#000000">Derived from Uniprot if available or header of the PDB structure.</font></td>
	</tr>
	<tr>
		<td rowspan=4 height="84" align="left" valign=middle><font color="#000000">Experimental data</font></td>
		<td align="left" valign=bottom><font color="#000000">T</font></td>
		<td align="left" valign=bottom><font color="#000000">T</font></td>
		<td align="left" valign=bottom><font color="#000000">no</font></td>
		<td align="left" valign=bottom><font color="#000000">Temperature of the experiment in Celsius.</font></td>
		<td align="left" valign=bottom><font color="#000000">Present in the original dataset. </font></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><font color="#000000">pH</font></td>
		<td align="left" valign=bottom><font color="#000000">pH</font></td>
		<td align="left" valign=bottom><font color="#000000">no</font></td>
		<td align="left" valign=bottom><font color="#000000">pH of the experiment.</font></td>
		<td align="left" valign=bottom><font color="#000000">Present in the original dataset. </font></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><font color="#000000">method</font></td>
		<td align="left" valign=bottom><font color="#000000">Method</font></td>
		<td align="left" valign=bottom><font color="#000000">no</font></td>
		<td align="left" valign=bottom><font color="#000000">Method of measuring the folding free energy change in the experiment.</font></td>
		<td align="left" valign=bottom><font color="#000000">Present in the original dataset. </font></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><font color="#000000">measure</font></td>
		<td align="left" valign=bottom><font color="#000000">Measure</font></td>
		<td align="left" valign=bottom><font color="#000000">no</font></td>
		<td align="left" valign=bottom><font color="#000000">Signal measured in the experiment.</font></td>
		<td align="left" valign=bottom><font color="#000000">Present in the original dataset. </font></td>
	</tr>
	<tr>
		<td height="21" align="left" valign=middle><font color="#000000">Source</font></td>
		<td align="left" valign=bottom><font color="#000000">reference</font></td>
		<td align="left" valign=bottom><font color="#000000">Reference</font></td>
		<td align="left" valign=bottom><font color="#000000">no</font></td>
		<td align="left" valign=bottom><font color="#000000">Experiment reference.</font></td>
		<td align="left" valign=bottom><font color="#000000">Present in the original dataset. </font></td>
	</tr>
	<tr>
		<td rowspan=2 height="42" align="left" valign=middle><font color="#000000">Additional data</font></td>
		<td align="left" valign=bottom><font color="#000000">dTm</font></td>
		<td align="left" valign=bottom><font color="#000000">&Delta;Tm</font></td>
		<td align="left" valign=bottom><font color="#000000">no</font></td>
		<td align="left" valign=bottom><font color="#000000">Change in protein melting temperature.</font></td>
		<td align="left" valign=bottom><font color="#000000">Present in the original dataset. </font></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><font color="#000000">notes</font></td>
		<td align="left" valign=bottom><font color="#000000">Notes</font></td>
		<td align="left" valign=bottom><font color="#000000">no</font></td>
		<td align="left" valign=bottom><font color="#000000">Additional comments.</font></td>
		<td align="left" valign=bottom><font color="#000000">Notes supplied with the original dataset were put here. Comments and errors are also reported here.</font></td>
	</tr>
</table>