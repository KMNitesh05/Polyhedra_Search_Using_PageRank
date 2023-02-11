#!/bin/bash
#SBATCH --partition=kamiak
#SBATCH -J ChemNetworks 
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --threads-per-core=1
#SBATCH --time=24:00:00
#SBATCH --array=1-500:1

#my_workspace="$(mkworkspace --quiet)"

#echo "My workspace is: $my_workspace"
#cd $my_workspace


cp ChemNetworks-2.2.exe ChemNetworks-2.2.${SLURM_ARRAY_TASK_ID}.exe
cp water_napolyhedra_final.input water_napolyhedra_final${SLURM_ARRAY_TASK_ID}.input

./ChemNetworks-2.2.${SLURM_ARRAY_TASK_ID}.exe water_napolyhedra_final${SLURM_ARRAY_TASK_ID}.input wat${SLURM_ARRAY_TASK_ID}.xyz na${SLURM_ARRAY_TASK_ID}.xyz


rm ChemNetworks-2.2.${SLURM_ARRAY_TASK_ID}.exe
rm water_napolyhedra_final${SLURM_ARRAY_TASK_ID}.input


