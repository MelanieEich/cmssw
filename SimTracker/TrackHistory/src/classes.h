#include "DataFormats/Common/interface/Wrapper.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "SimTracker/TrackHistory/interface/TrackCategories.h"
#include "SimTracker/TrackHistory/interface/VertexCategories.h"
#include "DataFormats/JetReco/interface/PFJet.h"

namespace SimTracker_TrackHistory {
  struct dictionary {
    // Dictionaires for Track and Vertex categories

    std::vector<TrackCategories> dummy01;
    std::vector<VertexCategories> dummy02;
    edm::Wrapper<std::vector<TrackCategories> > dummy03;
    edm::Wrapper<std::vector<VertexCategories> > dummy04;
    edm::Wrapper<reco::PFJet> dummy05;
    edm::Wrapper<reco::Jet> dummy06;
  };
}
