#ifndef CONDCORE_ORA_ORAHELPER
#define CONDCORE_ORA_ORAHELPER 1

#include "FWCore/Utilities/interface/TypeWithDict.h"
#include "FWCore/Utilities/interface/BaseWithDict.h"
#include "FWCore/Utilities/interface/MemberWithDict.h"
#include "RflxPropList.h"

namespace ora {
    namespace helper {
        
        size_t BaseSize(const edm::TypeWithDict& objType) {
            edm::TypeBases bases(objType);  // Type Bases is defined in TypeWithDict.h.
            return bases.size();
        } // end BaseSize
        
        edm::BaseWithDict BaseAt(const edm::TypeWithDict& objType, size_t index) {
            size_t indexWanted = index;
            size_t currentIndex = 0;
            edm::TypeBases bases(objType);
            edm::BaseWithDict baseWanted;
            for (auto const & b : bases) {
                if(currentIndex == indexWanted) {
                   baseWanted = edm::BaseWithDict(b);
                   break;
                }
                ++currentIndex;
            }
            return baseWanted;
        } // end BaseAt
        
        edm::MemberWithDict DataMemberAt(const edm::TypeWithDict& objType, size_t index) {
            size_t indexWanted = index;
            size_t currentIndex = 0;
            edm::TypeDataMembers bases(objType);
            edm::MemberWithDict baseWanted;
            for (auto const & b : bases) {
                if(currentIndex == indexWanted) {
                   baseWanted = edm::MemberWithDict(b);
                   break;
                }
                ++currentIndex;
            }
            return baseWanted;
        } // end DataMemberAt

        Reflex::PropertyList Properties( const edm::TypeWithDict& objType ) {
            // return Reflex::PropertyList( objType.qualifiedName() );
            Reflex::PropertyList pl; pl.setName( objType.qualifiedName() );
            return pl;
        }
        Reflex::PropertyList Properties( const edm::MemberWithDict& objType ) {
            // return Reflex::PropertyList( objType.qualifiedName() );
            Reflex::PropertyList pl; pl.setName( objType.typeOf().qualifiedName() );
            return pl;
        }

    } // end namespace helper
} // end namespace ora

#endif // CONDCORE_ORA_ORAHELPER
