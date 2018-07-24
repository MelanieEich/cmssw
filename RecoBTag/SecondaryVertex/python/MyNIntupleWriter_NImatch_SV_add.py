import FWCore.ParameterSet.Config as cms
import os
import copy

import SimTracker.TrackAssociatorProducers.trackAssociatorByHits_cfi as tabh

processName = "TruthMatchingPlot"
process = cms.Process(processName)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(40000) )

process.options   = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False),
    allowUnscheduled = cms.untracked.bool(True),
)

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("SimTracker.TrackHistory.VertexClassifier_cff")
process.vertexClassifier.vertexProducer = cms.untracked.InputTag("inclusiveSecondaryVertices")
process.vertexHistory.vertexProducer = cms.untracked.InputTag("inclusiveSecondaryVertices") 

process.ak4JetTracksAssociatorAtVertexPF = cms.EDProducer("JetTracksAssociatorAtVertex",
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.4),
    useAssigned = cms.bool(True),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    jets = cms.InputTag("ak4PFJetsCHS")
)


process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")
process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, "auto:run2_mc")

process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)

process.load("RecoBTag.ImpactParameter.impactParameterTagInfos_cfi")
process.impactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")

# SecondaryVertexProducer using IVF Vertex collection
process.load("RecoBTag.SecondaryVertex.secondaryVertexTagInfos_cfi")
process.secondaryVertexTagInfos.extSVCollection = cms.InputTag("inclusiveSecondaryVertices")
process.secondaryVertexTagInfos.vertexCuts.distVal2dMax = cms.double(99999.9)
process.secondaryVertexTagInfos.vertexCuts.distSig2dMin = cms.double(-99999.9)
process.vertexCutsBlock.vertexCuts.distVal2dMax = cms.double(99999.9)
process.vertexCutsBlock.vertexCuts.distSig2dMin = cms.double(-99999.9)
process.secondaryVertexTagInfos.useExternalSV = cms.bool(True)
process.secondaryVertexTagInfos.useSVClustering = cms.bool(True)
process.secondaryVertexTagInfos.jetAlgorithm = cms.string("AntiKt")
process.secondaryVertexTagInfos.rParam = cms.double(0.4)

process.load("SimTracker.TrackHistory.SecondaryVertexTagInfoProxy_cff")
process.svTagInfoProxy.svTagInfoProducer = cms.untracked.InputTag("secondaryVertexTagInfos")

process.load("PhysicsTools.UtilAlgos.TFileService_cfi")

process.svTagInfoValidation = cms.EDAnalyzer("SVTagInfoValidationAnalyzer",
    svTagInfoProducer = cms.untracked.InputTag("secondaryVertexTagInfos"),
    bestMatchByMaxValue = cms.untracked.bool(True),
    trackingTruth = cms.untracked.InputTag('mix','MergedTrackTruth'),
    vertexAssociator = cms.untracked.InputTag('vertexAssociatorByTracksByHits'),
    vertexProducer = cms.untracked.InputTag('svTagInfoProxy'),
    enableRecoToSim = cms.untracked.bool(True),
    enableSimToReco = cms.untracked.bool(False),
    hepMC = cms.untracked.InputTag("generatorSmeared"),
    longLivedDecayLength = cms.untracked.double(1e-14),
    vertexClusteringDistance = cms.untracked.double(0.003)
)


process.trackingParticleRecoTrackAsssociationByHits.associator = cms.InputTag("quickTrackAssociatorByHits")


process.vertexHistoryAnalyzer = cms.EDAnalyzer("VertexHistoryAnalyzer",
    process.vertexClassifier
)


# source for TTbar Spring2018 sample
process.source = cms.Source ("PoolSource",
    fileNames=cms.untracked.vstring(
#        'file:////pnfs/desy.de/cms/tier2/store/user/meich/NI_identification/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/TM_vertex/180712_124433/0000/vertex_TTbar18_default_test_few_13.root'
        'file:////pnfs/desy.de/cms/tier2/store/user/meich/NI_identification/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/TM_vertex/180720_080201/0000/vertex_TTbar18_default_5.root'
    )
)

process.out = cms.OutputModule("PoolOutputModule",
#    fileName = cms.untracked.string("/nfs/dust/cms/user/eichm/btag/ntuple/all_categ/vertex_TTbar_categ_13.root"
    fileName = cms.untracked.string("/nfs/dust/cms/user/eichm/btag/ntuple/all_categ/vertex_QCD_categ_5.root"),
#    fileName = cms.untracked.string("/store/user/meich/NI_identification/vertex_QCD_default_test.root"),
#    fileName = cms.untracked.string("vertex_TTbar18_default_test_few_SV.root"),
    outputCommands = cms.untracked.vstring("drop *",
                        "keep *_*_*_TruthMatching",
                        "keep *_*_*_TruthMatchingPlot",
                        "keep *_inclusiveSecondaryVertices_*_*",
                        "keep *_offlinePrimaryVertices_*_*",
                        "keep *_mix_MergedTrackTruth_*")
)


process.vertexAssociatorSequence = cms.Sequence(  process.vertexAssociatorByTracksByHits * process.impactParameterTagInfos * process.secondaryVertexTagInfos )

process.p = cms.Path(process.vertexAssociatorSequence * process.svTagInfoProxy * process.svTagInfoValidation)

process.e = cms.EndPath(process.out)

outFile = open("tmpConfig_vertex.py","w")
outFile.write(process.dumpPython())
outFile.close()
