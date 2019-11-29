#include <map>
#include <string>
#include <cmath>
#include <Math/Functions.h>
#include <Math/SVector.h>
#include <Math/SMatrix.h>
#include "TH1F.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TMath.h"
#include "DataFormats/BTauReco/interface/SecondaryVertexTagInfo.h"
#include "DataFormats/BTauReco/interface/CandSecondaryVertexTagInfo.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "SimTracker/TrackHistory/interface/VertexClassifierByProxy.h"
#include "CommonTools/Statistics/interface/ChiSquaredProbability.h"
#include "DataFormats/Math/interface/Vector.h"
#include "TROOT.h"
#include "Math/VectorUtil.h"
#include <TVector3.h>
#include <Math/GenVector/PxPyPzE4D.h>
#include <Math/GenVector/PxPyPzM4D.h>
#include "DataFormats/Math/interface/LorentzVector.h"

#include "SimTracker/TrackHistory/interface/VertexHistory.h"

#include "TFile.h"
#include "TTree.h"
#include "TBrowser.h"
#include "TSystem.h"
//
// class decleration
//
using namespace reco;
using namespace std;
using namespace edm;

class SVTagInfoValidationNImatchAnalyzer : public edm::one::EDAnalyzer<>
{

public:

    explicit SVTagInfoValidationNImatchAnalyzer(const edm::ParameterSet&);

private:

    void analyze(const edm::Event&, const edm::EventSetup&) override;
    void endJob() override ;
    // Member data

    VertexClassifierByProxy<reco::SecondaryVertexTagInfoCollection> classifier_;

    Int_t numberVertexClassifier_;
    edm::InputTag trackingTruth_;
    edm::InputTag svTagInfoProducer_;
    edm::InputTag secondaryVertices_;
  //    edm::InputTag fileName_;

    // Get the file service
    edm::Service<TFileService> fs_;

    Int_t n_event;
    Int_t rs_total_nall ; 
    Int_t rs_total_nsv ;
    Int_t rs_total_nbv ;
    Int_t rs_total_nbsv ;
    Int_t rs_total_ncv ;
    Int_t rs_total_nlv ;
    Int_t total_nfake ;

    Int_t sr_total_nall ; 
    Int_t sr_total_nsv ;
    Int_t sr_total_nbv ;
    Int_t sr_total_nbsv ;
    Int_t sr_total_ncv ;
    Int_t sr_total_nlv ;
    Int_t total_nmiss ;
        

  // Bookeeping of all the histograms per category
  void bookRecoToSim(std::string const &);
  void bookSimToReco(std::string const &);

  // Fill all histogram per category
  void fillRecoToSim(std::string const &, reco::Vertex const &, TrackingVertexRef const &);
  void fillSimToReco(std::string const &, reco::VertexBaseRef const &, TrackingVertexRef const &);

  // Histogram handlers
  std::map<std::string, TH1D *> TH1Index_;

  // Fill Tree with objects and Histograms
  TFile* output_;
  TString filename = "/nfs/dust/cms/user/eichm/btag/ntuple/vertex_QCD_class_NImatch.root";
  //  TString filename = "/vertex_QCD_test_classification.root";

  TTree * tree;
  std::vector<reco::Vertex> vertices_all_rs;
  std::vector<int> category_all_rs;
  std::vector<SimVertex> vertices_all_sr;
  std::vector<int> category_all_sr;


  std::vector<std::string> prepreNameHisto;
  std::vector<std::string> preNameHisto;
  std::vector<std::string> postNameHisto;
};


SVTagInfoValidationNImatchAnalyzer::SVTagInfoValidationNImatchAnalyzer(const edm::ParameterSet& config) : classifier_(config, consumesCollector())
{
  //Initialize counters
    n_event = 0;
    rs_total_nall = 0; 
    rs_total_nsv = 0;
    rs_total_nbv = 0;
    rs_total_nbsv = 0;
    rs_total_ncv = 0;
    rs_total_nlv = 0;
    total_nfake = 0;

    sr_total_nall = 0; 
    sr_total_nsv = 0;
    sr_total_nbv = 0;
    sr_total_nbsv = 0;
    sr_total_ncv = 0;
    sr_total_nlv = 0;
    total_nmiss = 0;

    //    usesResource("TFileService");

    prepreNameHisto.push_back("rs");
    //    prepreNameHisto.push_back("sr");
    preNameHisto.push_back("_All");
    preNameHisto.push_back("_SecondaryVertex");
    preNameHisto.push_back("_BSV");
    preNameHisto.push_back("_BWeakDecay");
    preNameHisto.push_back("_Ks");
    preNameHisto.push_back("_Fake");
    preNameHisto.push_back("_Light");
    //    postNameHisto.push_back("_MatchQuality");
    postNameHisto.push_back("_FlightDistance2d");
    postNameHisto.push_back("_nRecVtx");

    // Get the track collection
    svTagInfoProducer_ = config.getUntrackedParameter<edm::InputTag> ( "svTagInfoProducer" );
    consumes<reco::CandSecondaryVertexTagInfoCollection>(svTagInfoProducer_);

    // Name of the traking pariticle collection
    trackingTruth_ = config.getUntrackedParameter<edm::InputTag> ( "trackingTruth" );
    consumes<TrackingVertexCollection>(trackingTruth_);

    secondaryVertices_ = config.getUntrackedParameter<edm::InputTag> ( "secondaryVertices" );
    consumes<VertexCompositePtrCandidateCollection>(secondaryVertices_);

    // fileName_ = config.getUntrackedParameter<edm::InputTag>("fileName");
    // consumes<std::string>(fileName_);

    // edm::Handle<std::string> fileNa;
    // event.getByLabel(fileName_, fileNa);
    
    // filename = "/nfs/dust/cms/user/eichm/btag/ntuple/vertex_classification_"+fileNa+".root";

    // Number of track categories
    numberVertexClassifier_ = VertexCategories::Unknown+1;

    // Define histogram for counting categories
    TH1Index_["VertexClassifier"] = fs_->make<TH1D>(
                                        "VertexClassifier",
                                        "Frequency for the different track categories",
                                        numberVertexClassifier_,
                                        -0.5,
                                        numberVertexClassifier_ - 0.5
                                    );

    TH1Index_["VertexClassifier_sr"] = fs_->make<TH1D>(
						       "VertexClassifier_sr",
						       "Frequency for the different track categories",
						       numberVertexClassifier_,
						       -0.5,
                                        numberVertexClassifier_ - 0.5
						       );
    
    //--- RecoToSim
    TH1Index_["rs_All_MatchQuality"]= fs_->make<TH1D>( "rs_All_MatchQuality", "Quality of Match", 51, -0.01, 1.01 );
    TH1Index_["rs_All_FlightDistance2d"]= fs_->make<TH1D>( "rs_All_FlightDistance2d", "Transverse flight distance [cm]", 100, 0, 17 );
    TH1Index_["rs_SecondaryVertex_FlightDistance2d"]= fs_->make<TH1D>( "rs_SecondaryVertex_FlightDistance2d", "Transverse flight distance [cm]", 100, 0, 17 );
    TH1Index_["rs_BSV_FlightDistance2d"]= fs_->make<TH1D>( "rs_BSV_FlightDistance2d", "Transverse flight distance [cm]", 100, 0, 17 );
    TH1Index_["rs_BWeakDecay_FlightDistance2d"]= fs_->make<TH1D>( "rs_BWeakDecay_FlightDistance2d", "Transverse flight distance [cm]", 100, 0, 17 );
    TH1Index_["rs_CWeakDecay_FlightDistance2d"]= fs_->make<TH1D>( "rs_CWeakDecay_FlightDistance2d", "Transverse flight distance [cm]", 100, 0, 17 );
    TH1Index_["rs_Light_FlightDistance2d"]= fs_->make<TH1D>( "rs_Light_FlightDistance2d", "Transverse flight distance [cm]", 100, 0, 17 );
    TH1Index_["rs_Fake_FlightDistance2d"]= fs_->make<TH1D>( "rs_Fake_FlightDistance2d", "Transverse flight distance [cm]", 100, 0, 17 );
    TH1Index_["rs_Ks_FlightDistance2d"]= fs_->make<TH1D>( "rs_KshortDecay_FlightDistance2d", "Transverse flight distance [cm]", 100, 0, 17 );

    TH1Index_["rs_All_nRecVtx"]= fs_->make<TH1D>( "rs_All_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );
    TH1Index_["rs_SecondaryVertex_nRecVtx"]= fs_->make<TH1D>( "rs_SecondaryVertex_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );
    TH1Index_["rs_BSV_nRecVtx"]= fs_->make<TH1D>( "rs_BSV_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );
    TH1Index_["rs_BWeakDecay_nRecVtx"]= fs_->make<TH1D>( "rs_BWeakDecay_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );
    TH1Index_["rs_CWeakDecay_nRecVtx"]= fs_->make<TH1D>( "rs_CWeakDecay_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );
    TH1Index_["rs_Light_nRecVtx"]= fs_->make<TH1D>( "rs_Light_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );
    TH1Index_["rs_Ks_nRecVtx"]= fs_->make<TH1D>( "rs_Ks_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );
    TH1Index_["rs_Fake_nRecVtx"]= fs_->make<TH1D>( "rs_Fake_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );


    //--- SimToReco
    TH1Index_["sr_All_MatchQuality"]= fs_->make<TH1D>( "sr_All_MatchQuality", "Quality of Match", 51, -0.01, 1.01);
    TH1Index_["sr_All_nRecVtx"]= fs_->make<TH1D>( "sr_All_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );
    TH1Index_["sr_SecondaryVertex_nRecVtx"]= fs_->make<TH1D>( "sr_SecondaryVertex_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );
    TH1Index_["sr_BSV_nRecVtx"]= fs_->make<TH1D>( "sr_BSV_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );
    TH1Index_["sr_BWeakDecay_nRecVtx"]= fs_->make<TH1D>( "sr_BWeakDecay_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );
    TH1Index_["sr_CWeakDecay_nRecVtx"]= fs_->make<TH1D>( "sr_CWeakDecay_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );
    TH1Index_["sr_Light_nRecVtx"]= fs_->make<TH1D>( "sr_Light_nRecVtx", "Number of Vertices per event", 11, -0.5, 10.5 );  


    // Set the proper categories names
    for (Int_t i = 0; i < numberVertexClassifier_; ++i){
        TH1Index_["VertexClassifier"]->GetXaxis()->SetBinLabel(i+1, VertexCategories::Names[i]);
        TH1Index_["VertexClassifier_sr"]->GetXaxis()->SetBinLabel(i+1, VertexCategories::Names[i]);
    }

    // book histograms
    bookRecoToSim("rs_All");
    bookRecoToSim("rs_SecondaryVertex");
    bookRecoToSim("rs_BSV");
    bookRecoToSim("rs_BWeakDecay");
    bookRecoToSim("rs_CWeakDecay");
    bookRecoToSim("rs_Light");
    bookRecoToSim("rs_Ks");
    bookRecoToSim("rs_Fake");

    bookSimToReco("sr_All"); 
    bookSimToReco("sr_SecondaryVertex");
    bookSimToReco("sr_BSV");  
    bookSimToReco("sr_BWeakDecay");  
    bookSimToReco("sr_CWeakDecay");  
    bookSimToReco("sr_Light");  

    output_ = TFile::Open(filename,"RECREATE");
    //    output_ = new TFile(filename,"RECREATE");
    tree = new TTree("T","Categories");
    tree->Branch("Classifier_recosim", "std::vector<int>", &category_all_rs);
    tree->Branch("Vertices_recosim", "std::vector<reco::Vertex>", &vertices_all_rs);
    tree->Branch("Classifier_simreco", "std::vector<int>", &category_all_sr);
    tree->Branch("Vertices_simreco", "std::vector<SimVertex>", &vertices_all_sr);
}   


void SVTagInfoValidationNImatchAnalyzer::analyze(const edm::Event& event, const edm::EventSetup& setup)
{
  ++n_event;

  //  std::cout << "*** Analyzing " << event.id() << " n_event = " << n_event << std::endl << std::endl;

  // Set the classifier for a new event
  classifier_.newEvent(event, setup);
  

  // Vertex collection
  edm::Handle<reco::SecondaryVertexTagInfoCollection> svTagInfoCollection;
  event.getByLabel(svTagInfoProducer_, svTagInfoCollection);

  edm::Handle<reco::VertexCompositePtrCandidateCollection> secondaryVertices;
  event.getByLabel(secondaryVertices_, secondaryVertices);

  // Get a constant reference to the track history associated to the classifier
  VertexHistory const & tracer = classifier_.history();

  //  cout << "* Event " << n_event << " ; svTagInfoCollection->size() = " << svTagInfoCollection->size() << endl; 
  
  int rs_nall = 0; 
  int rs_nsv = 0;
  int rs_nbv = 0;
  int rs_nbsv = 0;
  int rs_ncv = 0;
  int rs_nlv = 0;
  int nfake = 0;

  int sr_nall = 0; 
  int sr_nsv = 0;
  int sr_nbv = 0;
  int sr_nbsv = 0;
  int sr_ncv = 0;
  int sr_nlv = 0;
  int nmiss = 0;

  vertices_all_rs.clear();
  category_all_rs.clear();
  vertices_all_sr.clear();
  category_all_sr.clear();

  std::cout << "size sV " << secondaryVertices->size() << std::endl;

  // Loop over the svTagInfo collection.
  for (std::size_t index = 0; index < svTagInfoCollection->size(); ++index){
    reco::SecondaryVertexTagInfoRef svTagInfo(svTagInfoCollection, index);

    if (svTagInfo->nVertices() > 0)    std::cout << "size sVTagInfo " << svTagInfo->nVertices() << std::endl;

    // Loop over the vertexes in svTagInfo
    for ( std::size_t vindex = 0; vindex < svTagInfo->nVertices(); ++vindex ){
      for (std::size_t indexSV = 0; indexSV < secondaryVertices->size(); ++ indexSV){
	reco::VertexCompositePtrCandidate sV = (*secondaryVertices)[indexSV];
	//	float dR = reco::deltaR(sV, svTagInfo->secondaryVertex(vindex));
	// std::cout << "sV p4 " << sV.p4() << std::endl;
	// std::cout << "sVTagInfo p4 " << svTagInfo->secondaryVertex(vindex).p4() << std::endl;
	// std::cout << "sV position " << sV.position() << std::endl;
	// std::cout << "sVTagInfo position " << svTagInfo->secondaryVertex(vindex).position() << std::endl;
	TVector3 vec(svTagInfo->secondaryVertex(vindex).x(), svTagInfo->secondaryVertex(vindex).y(), svTagInfo->secondaryVertex(vindex).z());
	std::cout << "sV eta " << sV.eta() << std::endl;
	std::cout << "sVTagInfo eta " << vec.PseudoRapidity() << std::endl;
	std::cout << "sV phi " << sV.phi() << std::endl;
	std::cout << "sVTagInfo phi " << vec.Phi() << std::endl;
	float p1 = sV.phi(); 
	float p2 = vec.Phi(); 
	float e1 = sV.eta(); 
	float e2 = vec.PseudoRapidity(); 
	auto dp=std::abs(p1-p2); if (dp>float(M_PI)) dp-=float(2*M_PI);  
	//	return (e1-e2)*(e1-e2) + dp*dp;
	std::cout << "dR " << ((e1-e2)*(e1-e2) + dp*dp) << std::endl;
	if (sV.p4() == svTagInfo->secondaryVertex(vindex).p4() and sV.position() == svTagInfo->secondaryVertex(vindex).position()){//dR < 0.01){
 
      // Classify the vertices
      classifier_.evaluate(svTagInfo, vindex);

      //quality of the match
      double rs_quality = tracer.quality();
 
      //      std::cout << "categories " << classifier_ << std::endl;

      // Fill the histogram with the categories
      for (Int_t i = 0; i != numberVertexClassifier_; ++i) {

	if ( classifier_.is( (VertexCategories::Category) i ) ) {

	  TH1Index_["VertexClassifier"]->Fill(i);
	  vertices_all_rs.push_back(svTagInfo->secondaryVertex(vindex));
          category_all_rs.push_back(i);
	}
      }
      if ( !classifier_.is(VertexCategories::Fake) && !classifier_.is(VertexCategories::Unknown) ) {

	//	cout << "R2S: MatchQuality = " << rs_quality << endl;

        TH1Index_["rs_All_MatchQuality"]->Fill( rs_quality );
	fillRecoToSim("rs_All", svTagInfo->secondaryVertex(vindex), tracer.simVertex());
	TH1Index_["rs_All_FlightDistance2d"]->Fill( svTagInfo->flightDistance( vindex, true ).value() );
        rs_nall++;

	if ( classifier_.is(VertexCategories::SecondaryVertex) ) {

	  //cout << "    R2S VertexCategories::SecondaryVertex" << endl;
	  fillRecoToSim("rs_SecondaryVertex", svTagInfo->secondaryVertex(vindex), tracer.simVertex());
	  TH1Index_["rs_SecondaryVertex_FlightDistance2d"]->Fill( svTagInfo->flightDistance( vindex, true ).value() );
          rs_nsv++;
	}
        
	if ( classifier_.is(VertexCategories::BWeakDecay) ) {

	  //cout << "    R2S VertexCategories::BWeakDecay" << endl;
	  fillRecoToSim("rs_BWeakDecay", svTagInfo->secondaryVertex(vindex), tracer.simVertex());
	  TH1Index_["rs_BWeakDecay_FlightDistance2d"]->Fill( svTagInfo->flightDistance( vindex, true ).value() );
          rs_nbv++;

          if ( classifier_.is(VertexCategories::SecondaryVertex) ) {
	    //cout << "    R2S VertexCategories::BWeakDecay SecondaryVertex" << endl;
	    fillRecoToSim("rs_BSV", svTagInfo->secondaryVertex(vindex), tracer.simVertex());
            TH1Index_["rs_BSV_FlightDistance2d"]->Fill( svTagInfo->flightDistance( vindex, true ).value() );
	    rs_nbsv++;	 

          }          
	}//BWeakDecay

	else if ( classifier_.is(VertexCategories::CWeakDecay) ) {

	  //cout << "    R2S VertexCategories::CWeakDecay" << endl;
	  fillRecoToSim("rs_CWeakDecay", svTagInfo->secondaryVertex(vindex), tracer.simVertex());
	  TH1Index_["rs_CWeakDecay_FlightDistance2d"]->Fill( svTagInfo->flightDistance( vindex, true ).value() );
          rs_ncv++;

	}
	else if ( classifier_.is(VertexCategories::KsDecay) ){
	  fillRecoToSim("rs_Ks", svTagInfo->secondaryVertex(vindex), tracer.simVertex());
	  TH1Index_["rs_Ks_FlightDistance2d"]->Fill( svTagInfo->flightDistance( vindex, true ).value() );
	}
	else {
	  //cout << "    R2S Light (rest of categories)" << endl;
	  //	  fillRecoToSim("rs_Light", svTagInfo->secondaryVertex(vindex), tracer.simVertex());
	  TH1Index_["rs_Light_FlightDistance2d"]->Fill( svTagInfo->flightDistance( vindex, true ).value() );
          rs_nlv++;
	}
      }//end if classifier

      else {
	//        cout << "    VertexCategories::Fake!!" << endl;
	// fillRecoToSim("rs_Fake", svTagInfo->secondaryVertex(vindex), tracer.simVertex());
	// TH1Index_["rs_Fake_FlightDistance2d"]->Fill( svTagInfo->flightDistance( vindex, true ).value() );
        nfake++;
      }
	} // end if loop for NI match
      } // end for loop over secondaryVertices

    }//end loop over vertices in svTagInfo

}//loop over svTagInfo

  tree->Fill();
  TH1Index_["rs_All_nRecVtx"]->Fill( rs_nall );
  TH1Index_["rs_SecondaryVertex_nRecVtx"]->Fill( rs_nsv );
  TH1Index_["rs_BWeakDecay_nRecVtx"]->Fill( rs_nbv );
  TH1Index_["rs_BSV_nRecVtx"]->Fill( rs_nbsv );
  TH1Index_["rs_CWeakDecay_nRecVtx"]->Fill( rs_ncv );  
  TH1Index_["rs_Light_nRecVtx"]->Fill( rs_nlv );  
  cout << endl;  

  //----------------------------------------------------------------
  // SIM TO RECO!

  // Vertex collection
  edm::Handle<TrackingVertexCollection>  TVCollection;
  event.getByLabel(trackingTruth_, TVCollection);
    
  // Loop over the TV collection.
  for (std::size_t index = 0; index < TVCollection->size(); ++index){
        
    TrackingVertexRef trackingVertex(TVCollection, index);

    classifier_.evaluate(trackingVertex);
 	
    double sr_quality = tracer.quality();

    // Fill the histogram with the categories
    for (Int_t i = 0; i != numberVertexClassifier_; ++i) {

      if ( classifier_.is( (VertexCategories::Category) i ) ) {
        TH1Index_["VertexClassifier_sr"]->Fill(i);
        //      vertices_all_sr.push_back(tracer.recoVertex());
        category_all_sr.push_back(i);
      }
    }
 
    if ( classifier_.is(VertexCategories::Reconstructed) && sr_quality>0. ) {

      //      cout << "S2R: MatchQuality = " << sr_quality << endl;
      TH1Index_["sr_All_MatchQuality"]->Fill( sr_quality );      
      //      fillSimToReco("sr_All", tracer.recoVertex(), trackingVertex);
      sr_nall++;

      if ( classifier_.is(VertexCategories::SecondaryVertex) ) {

	//cout << "    S2R VertexCategories::Reconstructed::SecondaryVertex" << endl;
	//        fillSimToReco("sr_SecondaryVertex", tracer.recoVertex(), trackingVertex);
        sr_nsv++;
      }

      if ( classifier_.is(VertexCategories::BWeakDecay) ) {

	//cout << "    S2R VertexCategories::Reconstructed::BWeakDecay" << endl;
	//        fillSimToReco("sr_BWeakDecay", tracer.recoVertex(), trackingVertex);
        sr_nbv++;

        if ( classifier_.is(VertexCategories::SecondaryVertex) ) {

	  //cout << "    S2R VertexCategories::Reconstructed::BWeakDecay SecondaryVertex" << endl;
	  //         fillSimToReco("sr_BSV", tracer.recoVertex(), trackingVertex);
         sr_nbsv++;
	}
    
      }//BWeakDecay

      else if ( classifier_.is(VertexCategories::CWeakDecay) ) {

	//cout << "    S2R VertexCategories::CWeakDecay" << endl;
	//	fillSimToReco("sr_CWeakDecay", tracer.recoVertex(), trackingVertex);
        sr_ncv++;
      }
 
      else {

	//cout << "    S2R Light (rest of categories)" << endl;
	//	fillSimToReco("sr_Light", tracer.recoVertex(), trackingVertex);
        sr_nlv++;
      }

    }//Reconstructed
    else {
      //cout << "##### Not reconstructed!" << endl;
      nmiss++;
    }

  }//TVCollection.size()

  TH1Index_["sr_All_nRecVtx"]->Fill( sr_nall );
  TH1Index_["sr_SecondaryVertex_nRecVtx"]->Fill( sr_nsv );
  TH1Index_["sr_BWeakDecay_nRecVtx"]->Fill( sr_nbv );
  TH1Index_["sr_BSV_nRecVtx"]->Fill( sr_nbsv );
  TH1Index_["sr_CWeakDecay_nRecVtx"]->Fill( sr_ncv );  
  TH1Index_["sr_Light_nRecVtx"]->Fill( rs_nlv );  

  rs_total_nall += rs_nall;  
  rs_total_nsv += rs_nsv;
  rs_total_nbv += rs_nbv;
  rs_total_nbsv += rs_nbsv;
  rs_total_ncv += rs_ncv ;
  rs_total_nlv += rs_nlv;
  total_nfake += nfake;

  sr_total_nall += sr_nall; 
  sr_total_nsv += sr_nsv;
  sr_total_nbv += sr_nbv;
  sr_total_nbsv += sr_nbsv;
  sr_total_ncv += sr_ncv;
  sr_total_nlv += sr_nlv;
  total_nmiss += nmiss;

}


void SVTagInfoValidationNImatchAnalyzer::bookRecoToSim(std::string const & prefix){
  // Book pull histograms

  std::string name = prefix + "_Pullx";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -10., 10.);
  name = prefix + "_Pully";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -10., 10.);
  name = prefix + "_Pullz";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -10., 10.);

   name = prefix + "_Resx";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -0.05, 0.05);
  name = prefix + "_Resy";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -0.05, 0.05); 
  name = prefix + "_Resz";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -0.05, 0.05); 

  name = prefix + "_Chi2Norm";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, 0, 10.); 
  name = prefix + "_Chi2Prob";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, 0., 1.); 
 
  name = prefix + "_nRecTrks";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 501, -0.5, 500.5);

  name = prefix + "_AverageTrackWeight";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -0.1, 1.1);

  name = prefix + "_Mass";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 65, 0., 6.5);

  name = prefix + "_RecPt";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 2000, 0., 1000.);

  name = prefix + "_RecEta";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 200, -3., 3.);

  name = prefix + "_RecCharge";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 21, -0.5, 20.5);

  name = prefix + "_RecTrackPt";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 2000, 0., 1000.);

  name = prefix + "_RecTrackEta";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 200, -3., 3.);

  name = prefix + "_nSimTrks";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 501, -0.5, 500.5); 

  name = prefix + "_SimPt";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 2000, 0., 1000.);

  name = prefix + "_SimEta";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 200, -3., 3.);

  name = prefix + "_SimCharge";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 21, -0.5, 20.5);
  
  name = prefix + "_SimTrackPt";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 500, 0., 500.);

  name = prefix + "_SimTrackEta";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 200, -3., 3.);


}


void SVTagInfoValidationNImatchAnalyzer::bookSimToReco(std::string const & prefix){
  // Book pull histograms

  std::string name = prefix + "_Pullx";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -10., 10.);
  name = prefix + "_Pully";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -10., 10.);
  name = prefix + "_Pullz";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -10., 10.);

   name = prefix + "_Resx";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -0.05, 0.05);
  name = prefix + "_Resy";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -0.05, 0.05); 
  name = prefix + "_Resz";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -0.05, 0.05); 

  name = prefix + "_Chi2Norm";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, 0, 10.); 
  name = prefix + "_Chi2Prob";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, 0., 1.); 
 
  name = prefix + "_nRecTrks";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 501, -0.5, 500.5);

  name = prefix + "_AverageTrackWeight";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 100, -0.1, 1.1);

  name = prefix + "_Mass";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 65, 0., 6.5);

  name = prefix + "_RecPt";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 2000, 0., 1000.);

  name = prefix + "_RecEta";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 200, -3., 3.);

  name = prefix + "_RecCharge";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 21, -0.5, 20.5);

  name = prefix + "_RecTrackPt";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 2000, 0., 1000.);

  name = prefix + "_RecTrackEta";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 200, -3., 3.);

  name = prefix + "_nSimTrks";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 501, -0.5, 500.5); 

  name = prefix + "_SimPt";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 2000, 0., 1000.);

  name = prefix + "_SimEta";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 200, -3., 3.);

  name = prefix + "_SimCharge";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 21, -0.5, 20.5);
  
  name = prefix + "_SimTrackPt";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 500, 0., 500.);

  name = prefix + "_SimTrackEta";
  TH1Index_[name] = fs_->make<TH1D>(name.c_str(), name.c_str(), 200, -3., 3.);


}


void SVTagInfoValidationNImatchAnalyzer::fillRecoToSim(std::string const & prefix, reco::Vertex const & vertex, TrackingVertexRef const & simVertex)
{
  double pullx = (vertex.x() - simVertex->position().x())/vertex.xError();
  double pully = (vertex.y() - simVertex->position().y())/vertex.yError();
  double pullz = (vertex.z() - simVertex->position().z())/vertex.zError();

  double resx = vertex.x() - simVertex->position().x();
  double resy = vertex.y() - simVertex->position().y();
  double resz = vertex.z() - simVertex->position().z();

  double chi2norm = vertex.normalizedChi2();
  double chi2prob = ChiSquaredProbability( vertex.chi2(), vertex.ndof() ); 

 double sum_weight = 0.;
 double weight = 0.;
 double tracksize =  vertex.tracksSize();
 math::XYZVector momentum;
 math::XYZTLorentzVector sum;
 int charge = 0;
 double thePiMass = 0.13957;

  for ( reco::Vertex::trackRef_iterator recDaughter = vertex.tracks_begin() ; recDaughter != vertex.tracks_end(); ++recDaughter) {

    ROOT::Math::LorentzVector<ROOT::Math::PxPyPzM4D<double> > vec;

    vec.SetPx( (**recDaughter).px() );
    vec.SetPy( (**recDaughter).py() );
    vec.SetPz( (**recDaughter).pz() );
    vec.SetM(thePiMass); 

    sum += vec;
  
    weight = vertex.trackWeight(*recDaughter); 
    sum_weight += weight;

    math::XYZVector p;
    p = (**recDaughter).momentum();
    momentum += p; 

    charge += (*recDaughter)->charge();

    TH1Index_[prefix + "_RecTrackPt"]->Fill( (*recDaughter)->pt() );
    TH1Index_[prefix + "_RecTrackEta"]->Fill( (*recDaughter)->eta() );      
  }//end loop to recDaughters
  //cout << "                   average sum of weights = " << sum_weight/tracksize << endl; 
  
  double mass = sum.M();
  double pt = sqrt( momentum.Perp2() );
  double eta = momentum.Eta();

  math::XYZVector simmomentum;
  int simcharge = 0;

  for ( TrackingVertex::tp_iterator simDaughter = simVertex->daughterTracks_begin(); simDaughter != simVertex->daughterTracks_end(); ++simDaughter ){

    math::XYZVector p;
    p = (**simDaughter).momentum();
    simmomentum += p; 

    simcharge += (*simDaughter)->charge();

    TH1Index_[prefix + "_SimTrackPt"]->Fill( (*simDaughter)->pt() );
    TH1Index_[prefix + "_SimTrackEta"]->Fill( (*simDaughter)->eta() );   
  }

  double simpt = sqrt( simmomentum.Perp2() );
  double simeta = simmomentum.Eta();

  //cout << "[fillRecoToSim]  vertex.tracksSize() = " << vertex.tracksSize() << " ; simVertex->nDaughterTracks() = " << simVertex->nDaughterTracks() << endl;  

  TH1Index_[prefix + "_nRecTrks"]->Fill( vertex.tracksSize() );
  TH1Index_[prefix + "_nSimTrks"]->Fill( simVertex->nDaughterTracks() );
  TH1Index_[prefix + "_Pullx"]->Fill(pullx);
  TH1Index_[prefix + "_Pully"]->Fill(pully);
  TH1Index_[prefix + "_Pullz"]->Fill(pullz);
  TH1Index_[prefix + "_Resx"]->Fill(resx);
  TH1Index_[prefix + "_Resy"]->Fill(resy);
  TH1Index_[prefix + "_Resz"]->Fill(resz);
  TH1Index_[prefix + "_AverageTrackWeight"]->Fill( sum_weight/tracksize );   
  TH1Index_[prefix + "_Chi2Norm"]->Fill(chi2norm);
  TH1Index_[prefix + "_Chi2Prob"]->Fill(chi2prob);
  TH1Index_[prefix + "_RecPt"]->Fill(pt);
  TH1Index_[prefix + "_RecEta"]->Fill(eta);
  TH1Index_[prefix + "_RecCharge"]->Fill(charge);
  TH1Index_[prefix + "_Mass"]->Fill(mass);
  TH1Index_[prefix + "_SimPt"]->Fill(simpt);
  TH1Index_[prefix + "_SimEta"]->Fill(simeta);
  TH1Index_[prefix + "_SimCharge"]->Fill(simcharge);  
}


void SVTagInfoValidationNImatchAnalyzer::fillSimToReco(std::string const & prefix, reco::VertexBaseRef const & vertex, TrackingVertexRef const & simVertex)
{

  double pullx = (vertex->x() - simVertex->position().x())/vertex->xError();
  double pully = (vertex->y() - simVertex->position().y())/vertex->yError();
  double pullz = (vertex->z() - simVertex->position().z())/vertex->zError();

  double resx = vertex->x() - simVertex->position().x();
  double resy = vertex->y() - simVertex->position().y();
  double resz = vertex->z() - simVertex->position().z();

  double chi2norm = vertex->normalizedChi2();
  double chi2prob = ChiSquaredProbability(vertex->chi2(), vertex->ndof()); 

  double sum_weight = 0.;
  double weight = 0.;
  double tracksize =  vertex->tracksSize();
  math::XYZVector momentum;
  math::XYZTLorentzVector sum;
  int charge = 0;
  double thePiMass = 0.13957;
  for ( reco::Vertex::trackRef_iterator recDaughter = vertex->tracks_begin() ; recDaughter != vertex->tracks_end(); ++recDaughter ) {

    ROOT::Math::LorentzVector<ROOT::Math::PxPyPzM4D<double> > vec;

    vec.SetPx( (**recDaughter).px() );
    vec.SetPy( (**recDaughter).py() );
    vec.SetPz( (**recDaughter).pz() );
    vec.SetM(thePiMass); 

    sum += vec;
  
    weight = vertex->trackWeight(*recDaughter); 
    sum_weight += weight;

    math::XYZVector p;
    p = (**recDaughter).momentum();
    momentum += p; 

    charge += (*recDaughter)->charge();

    TH1Index_[prefix + "_RecTrackPt"]->Fill( (*recDaughter)->pt() );
    TH1Index_[prefix + "_RecTrackEta"]->Fill( (*recDaughter)->eta() );  
  
  }
  //cout << "                   average sum of weights = " << sum_weight/tracksize << endl; 

  double mass = sum.M();
  double pt = sqrt( momentum.Perp2() );
  double eta = momentum.Eta();

   math::XYZVector simmomentum;
  int simcharge = 0;
  for ( TrackingVertex::tp_iterator simDaughter = simVertex->daughterTracks_begin(); simDaughter != simVertex->daughterTracks_end(); ++simDaughter ){

    math::XYZVector p;
    p = (**simDaughter).momentum();
    simmomentum += p; 

    simcharge += (*simDaughter)->charge();

    TH1Index_[prefix + "_SimTrackPt"]->Fill( (*simDaughter)->pt() );
    TH1Index_[prefix + "_SimTrackEta"]->Fill( (*simDaughter)->eta() );   
  }

  double simpt = sqrt( simmomentum.Perp2() );
  double simeta = simmomentum.Eta();

  //cout << "[fillSimToReco]  vertex->tracksSize() = " << vertex->tracksSize() << " ; simVertex->nDaughterTracks() = " << simVertex->nDaughterTracks() << endl;  

  TH1Index_[prefix + "_nRecTrks"]->Fill( vertex->tracksSize() );
  TH1Index_[prefix + "_nSimTrks"]->Fill( simVertex->nDaughterTracks() );
  TH1Index_[prefix + "_Pullx"]->Fill(pullx);
  TH1Index_[prefix + "_Pully"]->Fill(pully);
  TH1Index_[prefix + "_Pullz"]->Fill(pullz);
  TH1Index_[prefix + "_Resx"]->Fill(resx);
  TH1Index_[prefix + "_Resy"]->Fill(resy);
  TH1Index_[prefix + "_Resz"]->Fill(resz);
  TH1Index_[prefix + "_AverageTrackWeight"]->Fill( sum_weight/tracksize );   
  TH1Index_[prefix + "_Chi2Norm"]->Fill(chi2norm);
  TH1Index_[prefix + "_Chi2Prob"]->Fill(chi2prob);
  TH1Index_[prefix + "_RecPt"]->Fill(pt);
  TH1Index_[prefix + "_RecEta"]->Fill(eta);
  TH1Index_[prefix + "_RecCharge"]->Fill(charge);
  TH1Index_[prefix + "_Mass"]->Fill(mass);
  TH1Index_[prefix + "_SimPt"]->Fill(simpt);
  TH1Index_[prefix + "_SimEta"]->Fill(simeta);
  TH1Index_[prefix + "_SimCharge"]->Fill(simcharge);  

}


void 
SVTagInfoValidationNImatchAnalyzer::endJob() {

  output_->cd();
  for (unsigned int i=0; i<prepreNameHisto.size(); i++){
    for (unsigned int j=0; j<preNameHisto.size(); j++){
      for (unsigned int k=0; k<postNameHisto.size(); k++){
        TH1Index_[prepreNameHisto[i] + preNameHisto[j] + postNameHisto[k]]->Write();
      }
    }
  }

  TH1Index_["rs_All_MatchQuality"]->Write();
  TH1Index_["sr_All_MatchQuality"]->Write();
  TH1Index_["sr_All_nRecVtx"]->Write();
  TH1Index_["sr_SecondaryVertex_nRecVtx"]->Write();
  TH1Index_["sr_BWeakDecay_nRecVtx"]->Write();
  TH1Index_["sr_BSV_nRecVtx"]->Write();
  TH1Index_["sr_CWeakDecay_nRecVtx"]->Write();
  TH1Index_["sr_Light_nRecVtx"]->Write();
  TH1Index_["VertexClassifier"]->Write();
  TH1Index_["VertexClassifier_sr"]->Write();

  output_->Write();
  delete tree;
  delete output_;

  std::cout << std::endl;
  std::cout << " ====== Total Number of analyzed events: " << n_event << " ====== " << std::endl;
  std::cout << " ====== Total Number of R2S All:                         " << rs_total_nall << " ====== " << std::endl;
  std::cout << " ====== Total Number of R2S SecondaryVertex:             " << rs_total_nsv  << " ====== " << std::endl;
  std::cout << " ====== Total Number of R2S BWeakDecay:                  " << rs_total_nbv  << " ====== " << std::endl;
  std::cout << " ====== Total Number of R2S BWeakDecay::SecondaryVertex: " << rs_total_nbsv << " ====== " << std::endl;
  std::cout << " ====== Total Number of R2S CWeakDecay:                  " << rs_total_ncv  << " ====== " << std::endl;
  std::cout << " ====== Total Number of R2S Light:                       " << rs_total_nlv  << " ====== " << std::endl;
  std::cout << std::endl; 
  std::cout << " ====== Total Number of S2R All:                         " << sr_total_nall << " ====== " << std::endl;
  std::cout << " ====== Total Number of S2R SecondaryVertex:             " << sr_total_nsv  << " ====== " << std::endl;
  std::cout << " ====== Total Number of S2R BWeakDecay:                  " << sr_total_nbv  << " ====== " << std::endl;
  std::cout << " ====== Total Number of S2R BWeakDecay::SecondaryVertex: " << sr_total_nbsv << " ====== " << std::endl;
  std::cout << " ====== Total Number of S2R CWeakDecay:                  " << sr_total_ncv  << " ====== " << std::endl;
  std::cout << " ====== Total Number of S2R Light:                       " << sr_total_nlv  << " ====== " << std::endl;
  std::cout << std::endl; 
  std::cout << " ====== Total Number of Fake Vertices:              " << total_nfake   << " ====== " << std::endl;
 
} 


DEFINE_FWK_MODULE(SVTagInfoValidationNImatchAnalyzer);
