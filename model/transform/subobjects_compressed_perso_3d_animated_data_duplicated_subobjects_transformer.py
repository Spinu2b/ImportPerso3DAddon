import collections
import copy
import random
import string
from typing import Dict, List, Set
from model.perso.subobjects_compressed_perso_3d_animated_data import SubobjectsCompressedPerso3DAnimatedData

def generate_random_id() -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100))

class SubobjectsCompressedPerso3DAnimatedDataDuplicatedSubobjectsTransformer:
    def transform(self, perso3d_model: SubobjectsCompressedPerso3DAnimatedData):
        duplicated_objects_hashes = dict()  # type: Dict[str, int]
        for state_index in perso3d_model.states:
            for frame_number in perso3d_model.states[state_index]:
                objects_hashes_in_frame = [v.geometry_data_reference for v in perso3d_model.states[state_index][frame_number].data_blocks.values()]
                duplicated_objects_hashes_in_frame_with_counts = {item: count for item, count in collections.Counter(objects_hashes_in_frame).items() if count > 1}
                for duplicated_object_hash_in_frame in duplicated_objects_hashes_in_frame_with_counts:
                    if duplicated_object_hash_in_frame in duplicated_objects_hashes:

                        if duplicated_objects_hashes_in_frame_with_counts[duplicated_object_hash_in_frame] > duplicated_objects_hashes[duplicated_object_hash_in_frame]:
                            duplicated_objects_hashes[duplicated_object_hash_in_frame] = duplicated_objects_hashes_in_frame_with_counts[duplicated_object_hash_in_frame]
                    else:
                        duplicated_objects_hashes[duplicated_object_hash_in_frame] = duplicated_objects_hashes_in_frame_with_counts[duplicated_object_hash_in_frame]
        
        duplicated_objects_hashes_alternatives = dict()  # type: Dict[str, List[str]]
        for duplicated_object_hash in duplicated_objects_hashes:
            duplicated_objects_hashes_alternatives[duplicated_object_hash] = []
            for i in range(duplicated_objects_hashes[duplicated_object_hash] - 1):
                subobject_alternative_new_hash = generate_random_id()
                perso3d_model.subobjects[subobject_alternative_new_hash] = copy.deepcopy(perso3d_model.subobjects[duplicated_object_hash])
                perso3d_model.subobjects[subobject_alternative_new_hash].key = subobject_alternative_new_hash
                duplicated_objects_hashes_alternatives[duplicated_object_hash].append(subobject_alternative_new_hash)

        
        
        for state_index in perso3d_model.states:
            for frame_number in perso3d_model.states[state_index]:
                duplicated_objects_hashes_alternatives_to_use = copy.deepcopy(duplicated_objects_hashes_alternatives)
                already_encountered_hashes = []
                for subobject_key in perso3d_model.states[state_index][frame_number].data_blocks:

                    current_geometry_data_reference = perso3d_model.states[state_index][frame_number].data_blocks[subobject_key].geometry_data_reference

                    if current_geometry_data_reference in already_encountered_hashes:
                        new_hash_to_use = duplicated_objects_hashes_alternatives_to_use[current_geometry_data_reference].pop()
                        perso3d_model.states[state_index][frame_number].data_blocks[subobject_key].geometry_data_reference = new_hash_to_use

                    already_encountered_hashes.append(perso3d_model.states[state_index][frame_number].data_blocks[subobject_key].geometry_data_reference)

           
 