/*
 * Sev Data flex API v1.0
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;
using System.Runtime.Serialization;
using System.Text;
using System.Text.RegularExpressions;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Linq;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// FilterCustKwhMeteresReading
    /// </summary>
    [DataContract(Name = "FilterCustKwhMeteresReading")]
    public partial class FilterCustKwhMeteresReading : IEquatable<FilterCustKwhMeteresReading>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="FilterCustKwhMeteresReading" /> class.
        /// </summary>
        /// <param name="meters">meters.</param>
        /// <param name="fromDate">fromDate.</param>
        /// <param name="toDate">toDate.</param>
        public FilterCustKwhMeteresReading(List<int> meters = default(List<int>), DateTime fromDate = default(DateTime), DateTime toDate = default(DateTime))
        {
            this.Meters = meters;
            this.FromDate = fromDate;
            this.ToDate = toDate;
        }

        /// <summary>
        /// Gets or Sets Meters
        /// </summary>
        [DataMember(Name = "meters", EmitDefaultValue = true)]
        public List<int> Meters { get; set; }

        /// <summary>
        /// Gets or Sets FromDate
        /// </summary>
        [DataMember(Name = "from_date", EmitDefaultValue = false)]
        public DateTime FromDate { get; set; }

        /// <summary>
        /// Gets or Sets ToDate
        /// </summary>
        [DataMember(Name = "to_date", EmitDefaultValue = false)]
        public DateTime ToDate { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class FilterCustKwhMeteresReading {\n");
            sb.Append("  Meters: ").Append(Meters).Append("\n");
            sb.Append("  FromDate: ").Append(FromDate).Append("\n");
            sb.Append("  ToDate: ").Append(ToDate).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return Newtonsoft.Json.JsonConvert.SerializeObject(this, Newtonsoft.Json.Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as FilterCustKwhMeteresReading);
        }

        /// <summary>
        /// Returns true if FilterCustKwhMeteresReading instances are equal
        /// </summary>
        /// <param name="input">Instance of FilterCustKwhMeteresReading to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(FilterCustKwhMeteresReading input)
        {
            if (input == null)
            {
                return false;
            }
            return 
                (
                    this.Meters == input.Meters ||
                    this.Meters != null &&
                    input.Meters != null &&
                    this.Meters.SequenceEqual(input.Meters)
                ) && 
                (
                    this.FromDate == input.FromDate ||
                    (this.FromDate != null &&
                    this.FromDate.Equals(input.FromDate))
                ) && 
                (
                    this.ToDate == input.ToDate ||
                    (this.ToDate != null &&
                    this.ToDate.Equals(input.ToDate))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Meters != null)
                {
                    hashCode = (hashCode * 59) + this.Meters.GetHashCode();
                }
                if (this.FromDate != null)
                {
                    hashCode = (hashCode * 59) + this.FromDate.GetHashCode();
                }
                if (this.ToDate != null)
                {
                    hashCode = (hashCode * 59) + this.ToDate.GetHashCode();
                }
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
