# Dry run wrappers: This is a list of programs that are used in
# the exercises. When doing a dry run they get shadowed with a
# function only printing the command
declare -A Commands
# simput
Commands['fitshdr']=
Commands['HPXcvt']=
Commands['labnh']=
Commands['simputfile']=
Commands['simputimg']=
Commands['simputlc']=
Commands['simputmerge']=
Commands['simputmulticell']=
Commands['simputmultispec']=
Commands['simputpsd']=
Commands['simputrotate']=
Commands['simputspec']=
Commands['simputsrc']=
Commands['simputverify']=
Commands['sundazel']=
Commands['tofits']=
Commands['wcsgrid']=
Commands['wcsware']=

# sixte
Commands['athenawfisim']=
Commands['attgen_dither']=
Commands['comabackpro']=
Commands['comadet']=
Commands['comaexp']=
Commands['comaimg']=
Commands['comaimgPM']=
Commands['comaphovign']=
Commands['comarecon']=
Commands['epicmos1_events']=
Commands['epicmos2_events']=
Commands['epicpn_events']=
Commands['ero_calevents']=
Commands['ero_exposure']=
Commands['ero_fits2tm']=
Commands['ero_rawevents']=
Commands['erosim']=
Commands['ero_vis']=
Commands['evpat']=
Commands['exposure_map']=
Commands['fudgexp']=
Commands['gendetsim']=
Commands['gradeddetection']=
Commands['htrssim']=
Commands['imgev']=
Commands['ladsim']=
Commands['makelc']=
Commands['makespec']=
Commands['nustarsim']=
Commands['orbatt']=
Commands['pha2pi']=
Commands['phogen']=
Commands['phoimg']=
Commands['pixdetillum']=
Commands['piximpacts']=
Commands['projev']=
Commands['psfgen']=
Commands['pulsetemplgen']=
Commands['radec2xy']=
Commands['runmask']=
Commands['runsixt']=
Commands['runtes']=
Commands['sixte_arfgen']=
Commands['sixtesim']=
Commands['sixteversion']=
Commands['streamtotriggers']=
Commands['tesconstpileup']=
Commands['tesgenimpacts']=
Commands['tes_grades']=
Commands['tesstream']=
Commands['xifupipeline']=
Commands['xml2svg']=
Commands['xms_pixtemp']=

# Other tools
Commands['ftmerge']=
Commands['fstatistic']=
Commands['fhisto']=
Commands['isis']=
Commands['python']=
Commands['xspec']=
Commands['ln']=

shadow_cmds () {
  for cmd in "${!Commands[@]}" ; do
    if [ -z ${Commands[$cmd]} ] ; then
      eval "$(printf '%s() { echo %s $@ ; echo ; }' $cmd $cmd)"
    else
      eval "$(printf '%s() { %s }' $cmd ${Commands[$cmd]})"
    fi
    export -f "${cmd}"
  done
}
